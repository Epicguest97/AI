from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import requests
import getpass
import random
import urllib.parse
import re

def instagram_scraper(username, password, target_account, num_posts=10, download_stories=True):
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    # Add these options to make the browser less detectable
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    # Initialize webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Modify the User-Agent to make it look more like a regular browser
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    
    # Create directories to save the images
    if not os.path.exists("instagram_images"):
        os.makedirs("instagram_images")
    if not os.path.exists("instagram_stories"):
        os.makedirs("instagram_stories")
    
    try:
        # Open Instagram
        driver.get("https://www.instagram.com/")
        time.sleep(random.uniform(3, 5))  # Random wait to appear more human-like
        
        # Handle cookie consent if it appears
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow') or contains(text(), 'Accept') or contains(text(), 'Cookies')]"))
            )
            cookie_button.click()
            time.sleep(random.uniform(1, 3))
        except TimeoutException:
            print("No cookie prompt found or it has already been handled.")
        
        # Find username and password fields and login
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
        )
        password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        
        # Type like a human with random delays
        for char in username:
            username_field.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2))
            
        for char in password:
            password_field.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2))
            
        time.sleep(random.uniform(0.5, 1.5))
        password_field.send_keys(Keys.RETURN)
        time.sleep(random.uniform(5, 8))
        
        # Handle "Save Info" prompt if it appears
        try:
            not_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now') or contains(text(), 'Not now')]"))
            )
            not_now_button.click()
            time.sleep(random.uniform(1, 3))
        except TimeoutException:
            print("No 'Save Info' prompt found or it has already been handled.")
        
        # Handle notifications prompt if it appears
        try:
            not_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now') or contains(text(), 'Not now')]"))
            )
            not_now_button.click()
            time.sleep(random.uniform(1, 3))
        except TimeoutException:
            print("No notifications prompt found or it has already been handled.")
        
        # Navigate to target account
        driver.get(f"https://www.instagram.com/{target_account}/")
        time.sleep(random.uniform(4, 7))
        
        # Check if account exists and verify we can see content
        print(f"Checking access to {target_account}...")
        
        # First, check if we're on a valid profile page
        try:
            # Look for the profile username to confirm we're on a profile page
            profile_header = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, '_aacl')] | //h1 | //section//header//div//span"))
            )
            print(f"Found profile: {profile_header.text}")
            
            # Check if stories are available to download first (if requested)
            if download_stories:
                print("Checking for stories...")
                
                # Look for the story circle at the top of the profile
                story_selectors = [
                    "//div[contains(@class, '_aarf')]/div/canvas/..", # Canvas element in story circle
                    "//header//div[contains(@class, 'story')]",  # Generic story class
                    "//header//div[contains(@role, 'button')]//img[contains(@alt, 'profile picture')]/..",  # Profile picture that's clickable
                    "//div[contains(@role, 'button')]//img[@draggable='false' and contains(@alt, 'profile picture')]/.."  # Another common pattern
                ]
                
                story_element = None
                for selector in story_selectors:
                    try:
                        potential_elements = driver.find_elements(By.XPATH, selector)
                        for element in potential_elements:
                            # Take a screenshot of the area for debugging
                            try:
                                # Story circles usually have canvas element or specific styling
                                if element.is_displayed() and element.is_enabled():
                                    story_element = element
                                    break
                            except:
                                continue
                                
                        if story_element:
                            break
                    except:
                        continue
                        
                if story_element:
                    print("Found story element, attempting to view stories...")
                    try:
                        # Click on the story circle
                        driver.execute_script("arguments[0].click();", story_element)
                        time.sleep(random.uniform(3, 5))
                        
                        # Check if we successfully opened the story viewer
                        try:
                            story_viewer = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, "//div[contains(@role, 'dialog')] | //div[contains(@role, 'presentation')]"))
                            )
                            print("Story viewer opened successfully")
                            
                            # Download all stories
                            story_count = 0
                            max_stories = 20  # Safety limit
                            
                            while story_count < max_stories:
                                try:
                                    # Wait for story content to load
                                    time.sleep(random.uniform(1, 2))
                                    
                                    # Try to find video first (stories can be images or videos)
                                    try:
                                        video_element = WebDriverWait(driver, 3).until(
                                            EC.presence_of_element_located((By.XPATH, "//video[@src]"))
                                        )
                                        media_url = video_element.get_attribute('src')
                                        is_video = True
                                    except:
                                        # If no video, look for image
                                        try:
                                            image_element = WebDriverWait(driver, 3).until(
                                                EC.presence_of_element_located((By.XPATH, "//div[contains(@role, 'dialog')]//img[not(contains(@alt, 'profile'))]"))
                                            )
                                            media_url = image_element.get_attribute('src')
                                            is_video = False
                                        except:
                                            print("Could not find media in story")
                                            media_url = None
                                            is_video = False
                                    
                                    if media_url:
                                        story_count += 1
                                        # Download the media
                                        media_response = requests.get(media_url)
                                        if media_response.status_code == 200:
                                            extension = "mp4" if is_video else "jpg"
                                            filename = f"instagram_stories/{target_account}_story_{story_count}.{extension}"
                                            with open(filename, 'wb') as file:
                                                file.write(media_response.content)
                                            print(f"Downloaded story {story_count}: {filename}")
                                        else:
                                            print(f"Failed to download story {story_count}: HTTP {media_response.status_code}")
                                    
                                    # Find and click the next button
                                    next_button_selectors = [
                                        "//button[contains(@aria-label, 'Next')]",
                                        "//div[@role='button' and contains(@aria-label, 'Next')]",
                                        "//div[contains(@role, 'dialog')]//div[@role='button' and @aria-label]"
                                    ]
                                    
                                    next_clicked = False
                                    for selector in next_button_selectors:
                                        try:
                                            buttons = driver.find_elements(By.XPATH, selector)
                                            # Usually the right side button is for "next"
                                            if len(buttons) > 1:
                                                next_button = buttons[-1]  # Last button is usually "next"
                                            elif len(buttons) == 1:
                                                next_button = buttons[0]
                                            else:
                                                continue
                                                
                                            # Click the next button
                                            driver.execute_script("arguments[0].click();", next_button)
                                            next_clicked = True
                                            time.sleep(random.uniform(1, 2))
                                            break
                                        except Exception as e:
                                            continue
                                    
                                    # If we couldn't click "next", we've reached the end
                                    if not next_clicked:
                                        print("Reached the end of stories or couldn't find next button")
                                        break
                                        
                                except Exception as e:
                                    print(f"Error processing story: {e}")
                                    break
                            
                            print(f"Downloaded {story_count} stories")
                            
                            # Close story viewer
                            try:
                                close_button = WebDriverWait(driver, 5).until(
                                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Close')] | //div[@role='button' and contains(@aria-label, 'Close')]"))
                                )
                                close_button.click()
                            except:
                                # Try pressing Escape key
                                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                                
                            time.sleep(random.uniform(2, 3))
                            
                            # Navigate back to profile page
                            driver.get(f"https://www.instagram.com/{target_account}/")
                            time.sleep(random.uniform(3, 5))
                            
                        except Exception as e:
                            print(f"Error with story viewer: {e}")
                            # Take a screenshot for debugging
                            driver.save_screenshot("story_error.png")
                            print("Story error screenshot saved as 'story_error.png'")
                            
                            # Navigate back to profile page
                            driver.get(f"https://www.instagram.com/{target_account}/")
                            time.sleep(random.uniform(3, 5))
                            
                    except Exception as e:
                        print(f"Error clicking on story circle: {e}")
                else:
                    print("No active stories found for this account")
            
            # Now proceed with downloading posts
            # Check if we can see the post grid
            try:
                # Try multiple selectors for posts as Instagram changes them often
                post_selectors = [
                    "article a", 
                    "article div[role='button']", 
                    "main article a", 
                    "div[role='tablist'] + div article a",
                    "//div[contains(@class, '_aagw')]",
                    "//div[contains(@class, '_aabd')]//a",
                    "//article//a[contains(@href, '/p/')]"
                ]
                
                post_found = False
                for selector in post_selectors:
                    try:
                        if selector.startswith("//"):
                            posts = driver.find_elements(By.XPATH, selector)
                        else:
                            posts = driver.find_elements(By.CSS_SELECTOR, selector)
                        
                        if posts:
                            print(f"Found {len(posts)} posts using selector: {selector}")
                            post_found = True
                            break
                    except:
                        continue
                
                if not post_found:
                    # Try scrolling down to load content
                    print("No posts found initially, scrolling to load content...")
                    driver.execute_script("window.scrollTo(0, 300);")
                    time.sleep(3)
                    
                    # Check again after scrolling
                    for selector in post_selectors:
                        try:
                            if selector.startswith("//"):
                                posts = driver.find_elements(By.XPATH, selector)
                            else:
                                posts = driver.find_elements(By.CSS_SELECTOR, selector)
                            
                            if posts:
                                print(f"Found {len(posts)} posts after scrolling using selector: {selector}")
                                post_found = True
                                break
                        except:
                            continue
                
                if not post_found:
                    # If still no posts found, check if we're on a private account page
                    try:
                        private_message = driver.find_element(By.XPATH, "//h2[contains(text(), 'Private') or contains(text(), 'private')]")
                        print("This is a private account.")
                        
                        # Check if there's a "Follow" button (means we don't follow them)
                        try:
                            follow_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Follow') or contains(text(), 'follow')]")
                            print("You don't follow this account. Please follow them first.")
                            return
                        except NoSuchElementException:
                            print("You seem to follow this account but can't see posts. Instagram might be restricting access.")
                            # Take screenshot for debugging
                            driver.save_screenshot("debug_screenshot.png")
                            print("Debug screenshot saved as 'debug_screenshot.png'")
                    except NoSuchElementException:
                        print("Unable to determine if this is a private account.")
                        # Take screenshot for debugging
                        driver.save_screenshot("debug_screenshot.png")
                        print("Debug screenshot saved as 'debug_screenshot.png'")
                
            except Exception as e:
                print(f"Error checking for posts: {e}")
                driver.save_screenshot("error_screenshot.png")
                print("Error screenshot saved as 'error_screenshot.png'")
                return
            
        except Exception as e:
            print(f"Error checking for posts: {e}")
            driver.save_screenshot("error_screenshot.png")
            print("Error screenshot saved as 'error_screenshot.png'")
            return
            
        except Exception as e:
            print(f"Error: Could not access account '{target_account}'. Error: {e}")
            return
        
        # Continue with post collection
        post_links = []
        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_attempts = 0
        max_scroll_attempts = 5
        
        while len(post_links) < num_posts and scroll_attempts < max_scroll_attempts:
            scroll_attempts += 1
            
            # Try multiple selectors to find posts
            post_selectors = [
                "//a[contains(@href, '/p/')]",
                "//div[contains(@class, '_aagw')]//a",
                "//article//a[contains(@href, '/p/')]",
                "//div[contains(@class, '_aabd')]//a"
            ]
            
            for selector in post_selectors:
                try:
                    posts = driver.find_elements(By.XPATH, selector)
                    
                    for post in posts:
                        try:
                            post_url = post.get_attribute('href')
                            if post_url and '/p/' in post_url and post_url not in post_links:
                                post_links.append(post_url)
                                print(f"Found post: {post_url}")
                                
                            if len(post_links) >= num_posts:
                                break
                        except Exception as e:
                            print(f"Error processing post element: {e}")
                            continue
                    
                    if posts and not post_links:
                        print(f"Found {len(posts)} elements with selector {selector} but couldn't extract links")
                        
                    if len(post_links) >= num_posts:
                        break
                        
                except Exception as e:
                    print(f"Error with selector {selector}: {e}")
                    continue
            
            # If we've found some posts, break the loop
            if post_links:
                break
                
            # Scroll down
            print(f"Scrolling attempt {scroll_attempts}/{max_scroll_attempts}...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 4))
            
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("Reached end of page or content not loading")
                break
            last_height = new_height
        
        if not post_links:
            print("Could not find any posts. Instagram may be hiding content or the account might not have posts.")
            driver.save_screenshot("no_posts_screenshot.png")
            print("Screenshot saved as 'no_posts_screenshot.png'")
            return
            
        print(f"Found {len(post_links)} posts, downloading...")
        
        # Visit each post and download the image
        for i, post_url in enumerate(post_links):
            driver.get(post_url)
            time.sleep(random.uniform(2, 4))
            
            try:
                # Try multiple selectors for images
                img_selectors = [
                    "//article//img[@class and not(contains(@alt, 'profile'))]",
                    "//div[contains(@role, 'dialog')]//img[not(contains(@alt, 'profile'))]",
                    "//div[contains(@class, '_aagv')]//img",
                    "//article//div[contains(@role, 'button')]//img"
                ]
                
                img_found = False
                for selector in img_selectors:
                    try:
                        img_element = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, selector))
                        )
                        img_url = img_element.get_attribute('src')
                        
                        if img_url:
                            img_found = True
                            # Download the image
                            img_response = requests.get(img_url)
                            if img_response.status_code == 200:
                                filename = f"instagram_images/{target_account}_post_{i+1}.jpg"
                                with open(filename, 'wb') as file:
                                    file.write(img_response.content)
                                print(f"Downloaded: {filename}")
                            else:
                                print(f"Failed to download image from post #{i+1}: HTTP {img_response.status_code}")
                            break
                    except Exception as e:
                        print(f"Error with image selector {selector}: {e}")
                        continue
                
                if not img_found:
                    print(f"Could not find image in post #{i+1}")
            
            except Exception as e:
                print(f"Error processing post #{i+1}: {e}")
            
            # Add random delay between posts to mimic human behavior
            time.sleep(random.uniform(1, 3))
        
        print("Scraping completed!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot("error_screenshot.png")
        print("Error screenshot saved as 'error_screenshot.png'")
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    print("Instagram Post and Story Scraper")
    print("---------------------")
    
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")
    target_account = input("Enter the account to scrape: ")
    
    try:
        num_posts = int(input("How many posts to download? (default: 10): ") or 10)
    except ValueError:
        num_posts = 10
        
    download_stories = input("Download stories? (y/n, default: y): ").lower() != 'n'
    
    instagram_scraper(username, password, target_account, num_posts, download_stories)