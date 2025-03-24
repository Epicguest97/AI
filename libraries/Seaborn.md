# Introduction to Seaborn
What is Seaborn?: Seaborn is a Python visualization library based on Matplotlib that provides a high-level interface for drawing attractive statistical graphics.
Why Seaborn?: Seaborn is easier to use for statistical plots and comes with enhanced default styles and color palettes.

# Basic Plotting with Seaborn
Line Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data: seaborn's built-in dataset
tips = sns.load_dataset("tips")

# Line plot: Total bill vs. tip, grouped by time
sns.lineplot(x="total_bill", y="tip", data=tips)
plt.title("Line Plot - Total Bill vs Tip")
plt.show()
```
Scatter Plot
```python
# Scatter plot with Seaborn
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="time", style="time")
plt.title("Scatter Plot - Total Bill vs Tip")
plt.show()
```
# Customizing Plots in Seaborn
Customizing Colors
```python

# Customizing colors using Seaborn
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex", palette="coolwarm")
plt.title("Custom Colored Scatter Plot")
plt.show()
```
Adding Regression Line
```python
# Scatter plot with regression line
sns.regplot(x="total_bill", y="tip", data=tips, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Scatter Plot with Regression Line")
plt.show()
```
# Distribution Plots
Histogram
```python
# Histogram plot
sns.histplot(tips["total_bill"], kde=True, color="green")
plt.title("Histogram - Total Bill Distribution")
plt.show()
```
Box Plot
```python
# Box plot to show distribution of total_bill by time
sns.boxplot(x="time", y="total_bill", data=tips, palette="Set2")
plt.title("Box Plot - Total Bill by Time")
plt.show()
```
Violin Plot
```python
# Violin plot to show distribution and KDE for total_bill by time
sns.violinplot(x="time", y="total_bill", data=tips, palette="muted")
plt.title("Violin Plot - Total Bill by Time")
plt.show()
```
5. Categorical Plots
Bar Plot
```python
# Bar plot showing the average total_bill by day
sns.barplot(x="day", y="total_bill", data=tips, palette="Blues")
plt.title("Bar Plot - Average Total Bill by Day")
plt.show()
```
Count Plot
```python
# Count plot showing the count of orders by day
sns.countplot(x="day", data=tips, palette="Set1")
plt.title("Count Plot - Orders by Day")
plt.show()
```
# Pair Plots (Pairwise Relationships)
```python
# Pair plot showing relationships between numerical columns
sns.pairplot(tips, hue="sex", palette="coolwarm")
plt.title("Pair Plot - Relationships Between Numerical Columns")
plt.show()
```
# Heatmap
```python
# Heatmap showing correlation matrix of numerical columns
corr_matrix = tips.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap - Correlation Matrix")
plt.show()
```
# FacetGrid and PairGrid
FacetGrid
```python
# FacetGrid to show scatter plots for different days
g = sns.FacetGrid(tips, col="time", row="sex", margin_titles=True)
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
plt.show()
```
PairGrid
```python
# PairGrid to show scatter plots of total_bill vs tip, grouped by time
g = sns.PairGrid(tips, hue="time")
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.add_legend()
plt.show()
```
# Statistical Plotting
Bar Plot with Error Bars
```python
# Bar plot showing the mean total_bill by day with error bars
sns.barplot(x="day", y="total_bill", data=tips, ci="sd", palette="pastel")
plt.title("Bar Plot with Error Bars - Total Bill by Day")
plt.show()
```
Heatmap for Categorical Data
```python
# Heatmap for categorical data using pivot_table
pivot = tips.pivot_table(values="tip", index="day", columns="time", aggfunc="mean")
sns.heatmap(pivot, annot=True, cmap="Blues")
plt.title("Heatmap - Tips by Day and Time")
plt.show()
```
# Advanced Plots
Joint Plot
```python
# Joint plot showing the relationship between total_bill and tip, with histograms on the sides
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex", color="purple")
plt.title("Joint Plot - Total Bill vs Tip")
plt.show()
```
Rug Plot
```python
# Rug plot showing the distribution of total_bill
sns.rugplot(tips["total_bill"], color="red")
plt.title("Rug Plot - Total Bill Distribution")
plt.show()
```
# Saving Seaborn Plots
```python
# Save a Seaborn plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Scatter Plot - Total Bill vs Tip")
plt.savefig("seaborn_scatter_plot.png")  # Save the plot as an image
plt.show()
```