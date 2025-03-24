# Introduction to Matplotlib
What is Matplotlib?:
- An introduction to Matplotlib as a plotting library for Python, widely used for creating static, animated, and interactive visualizations.
- Why Matplotlib?: Discuss its importance for data visualization in data science and its compatibility with other libraries like Pandas and NumPy.

# Basic Plotting with Matplotlib
Creating Basic Plots:

- plt.plot(): Line plot for simple data visualization.
Example implementation: Plot a simple line graph for a mathematical function like y = x^2.
Customizing Plots:

- Titles, labels, and legends: plt.title(), plt.xlabel(), plt.ylabel(), plt.legend().
Example implementation: Create a plot for a dataset with proper labels and a title.
Grid and Axis Customization:

- Displaying grids with plt.grid().
Adjusting axes with plt.xlim() and plt.ylim().
Example implementation:

## Basic Plotting with Matplotlib

```python
# Simple line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
```
# Customizing Plots

```python 
# Customize a plot with title, labels, and legend
plt.plot(x, y, label="y = x^2", color='r', linestyle='--', marker='o')
plt.title("Customized Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)
plt.show()
```
# Types of Plots in Matplotlib
Basic line plot and multiple lines on the same plot.
Example implementation: Plot multiple functions on the same graph (e.g., sin(x), cos(x)).
```python
# Plotting multiple lines
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.title("Sine and Cosine Functions")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)
plt.show()
```
Scatter Plot:
Creating scatter plots using plt.scatter().
Example implementation: Scatter plot of random data points.
```python
# Scatter plot with random data
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color='blue', alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()
```
Bar Plot:

Vertical and horizontal bar charts using plt.bar() and plt.barh().
Example implementation: A bar plot showing the frequency of categories in a dataset.
```python
# Bar chart for categorical data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 18]
plt.bar(categories, values, color='green')
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(True)
plt.show()
```
Histogram:

Using plt.hist() for frequency distributions.
Example implementation: Plotting a histogram for random normal data.
```python
# Histogram of random data
data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
```
Pie Chart:

Using plt.pie() for pie charts.
Example implementation: Pie chart of a dataset’s category proportions.
```python
# Pie chart showing proportions
sizes = [20, 30, 50]
labels = ['Category A', 'Category B', 'Category C']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.show()
```
Box Plot:

Using plt.boxplot() to visualize data distributions and outliers.
Example implementation: Box plot for the distribution of scores in a class.

```python
import numpy as np
# Box plot showing data distribution
data = np.random.randn(100)
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

```

# Subplots and Multiple Figures
Subplots:

Creating multiple subplots in a single figure using plt.subplot() or plt.subplots().
Example implementation: Displaying multiple plots in a grid (e.g., line plot and scatter plot in one figure).
Figures and Axes:

Creating separate figures and axes for more advanced layouts.
Example implementation: Create a figure with two different types of plots.
```python
# Subplots: Multiple plots in a single figure
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].plot(x, y1, label="sin(x)")
axes[0].set_title("Sine Function")
axes[0].grid(True)

axes[1].plot(x, y2, label="cos(x)", color='orange')
axes[1].set_title("Cosine Function")
axes[1].grid(True)

plt.tight_layout()
plt.show()
```
# Customization and Styling
Colors and Styles:

Changing line colors, styles, and markers (e.g., color, linestyle, marker).
Example implementation: Customizing a plot with different line styles and markers.
Fonts and Text:

Adding custom fonts and text annotations with plt.text() and plt.annotate().
Example implementation: Annotating specific points on a plot.
Ticks and Labels:

Customizing ticks and labels on the x and y axes using plt.xticks() and plt.yticks().
Example implementation: Rotating tick labels and adjusting their frequency.
```python
# Styling and customization of the plot
plt.plot(x, y, label="y = x^2", color='red', linestyle='-.', marker='x', markersize=10)
plt.title("Customized Line Plot with Style")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
```
# Advanced Visualization Techniques
Logarithmic Scale:

Creating logarithmic plots with plt.yscale('log') or plt.xscale('log').
Example implementation: Plotting exponential data on a logarithmic scale.
Heatmaps:

Visualizing data using imshow() or pcolor().
Example implementation: Displaying a heatmap for a 2D array of values.
3D Plotting:

Creating 3D plots using Axes3D for 3D scatter, surface, and wireframe plots.
Example implementation: Plotting a 3D surface for a mathematical function.
```python
from mpl_toolkits.mplot3d import Axes3D

# 3D surface plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D Surface Plot")
plt.show()

```
# Saving and Exporting Figures
Saving Plots:

Saving the plot to files like PNG, JPG, or PDF using plt.savefig().
Example implementation: Save a plot to a file.
Interactive Plots:

Using plt.show() to display plots interactively in Jupyter Notebook or other environments.
Example implementation: Plotting and interacting with the graph.
```python
# Save the plot as an image file
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.savefig('line_plot.png')  # Save as PNG file
plt.show()

```
# Integration with Pandas and NumPy
Pandas Integration:
Plotting directly from Pandas DataFrames using .plot().
Example implementation: Plotting a DataFrame of financial data with dates on the x-axis.
```python
import pandas as pd

# Create a DataFrame
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Sales': [100, 120, 150, 170, 180]}

df = pd.DataFrame(data)

# Plot directly from DataFrame
df.plot(x='Year', y='Sales', kind='line', marker='o', color='b')
plt.title("Sales Over Years (Pandas Plotting)")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
```
NumPy Integration:
Using NumPy arrays as inputs for Matplotlib.
Example implementation: Plot a sine wave using NumPy arrays and Matplotlib.
```python
# Using NumPy to create data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot a sine wave using NumPy data
plt.plot(x, y)
plt.title("Sine Wave (NumPy Data)")
plt.xlabel("X values")
plt.ylabel("sin(X)")
plt.grid(True)
plt.show()

```
