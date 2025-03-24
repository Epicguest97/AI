# Report on Pandas

 Pandas  offers a structured approach to mastering data
manipulation in Python. It covers several key topics that build a strong
foundation for working with data efficiently and effectively. Below is a
detailed exploration of the key subtopics from the course:

**1. Creating, Reading, and Writing Data**

With an introduction to Pandas\' two fundamental data
structures: **Series** and **DataFrames**. A **Series** is a
one-dimensional array-like structure, while a **DataFrame** is a
two-dimensional, tabular structure that allows you to store data in rows
and columns, much like a spreadsheet or SQL table.

This section also covers how to read and write data to and from external
files, particularly CSV files. The pd.read_csv() function is widely used
to import data into a Pandas DataFrame, and to_csv() is used to export
data back into CSV format after manipulation. These capabilities make
Pandas a convenient tool for handling large datasets with ease, enabling
seamless data flow between different stages of analysis​.

# Implement
```python
# 1. Creating a Series
# From a list
series_from_list = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# From a dictionary
data_dict = {'x': 100, 'y': 200, 'z': 300}
series_from_dict = pd.Series(data_dict)
# From a NumPy array
array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(array, index=['A', 'B', 'C', 'D', 'E'])
# for file
csv_series = pd.read_csv('data.csv')['values']
```
for dataframes-
```python
# 1. Creating a DataFrame
# From a dictionary of lists
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85.5, 90.0, 88.5]
}
dataframe_from_dict = pd.DataFrame(data_dict)
# for file
dataframe_from_csv = pd.read_csv('data.csv')
# From a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dataframe_from_array = pd.DataFrame(array, columns=['A', 'B', 'C'])
```

**2. Indexing, Selecting, and Assigning**

Understanding how to efficiently access and manipulate data is crucial
for any data analysis task. The course dives into **indexing** and
**selecting** data, which allows users to target specific parts of the
dataset. Functions like .loc\[\] and .iloc\[\] are introduced for
selecting data by label or by position, respectively.

Moreover,  conditional selections can be made,
where only rows that meet certain criteria are returned. For example,
using .loc\[\] to filter rows based on conditions like greater-than or
less-than values. This feature is analogous to filtering data in SQL,
making it an essential skill for navigating through large datasets.

Assignments can also be done easily, meaning values within the DataFrame
can be updated or new columns can be created based on existing data​

```python
# 2. Indexing and Slicing
# Accessing elements by index
print("\nElement at index 'b' in series_from_list:", series_from_list['b'])

# Slicing
print("\nSlicing series_from_list (indices 'b' to 'd'):\n", series_from_list['b':'d'])

# Boolean indexing
filtered_series = series_from_list[series_from_list > 20]
print("\nFiltered series (values > 20):\n", filtered_series)
# Dropping a column
dropped_column_df = dataframe_from_dict.drop(columns=['Passed'])
# Using .loc and .iloc
print("\nRow selection with .loc (Name and Age columns for index 1):\n", df.loc[1, ['Name', 'Age']])
print("\nRow selection with .iloc (first two rows, first two columns):\n", df.iloc[:2, :2])
```
**3. Summary Functions and Maps**

Once data has been loaded and cleaned, summarizing it is the next
logical step. This part of the course introduces **summary functions**
like mean(), median(), sum(), and describe(). These functions enable
quick statistical analysis, providing insights such as the average,
total, or count of data within columns. The describe() function is
particularly useful as it provides a comprehensive summary of central
tendencies, spread, and shape of the data's distribution, all in one go.

Additionally, the **map()** function allows for applying a
transformation to an entire Series. This comes in handy when values in a
column need to be modified or mapped to new values based on a function,
making transformations straightforward and efficient​
```python 
sum_value = df['Value'].sum()  # Sum of values
mean_value = df['Value'].mean()  # Mean of values
max_value = df['Value'].max()  # Maximum value
grouped = df.groupby('Category')['Value'].mean()
```
```python
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcategory': ['X', 'X', 'Y', 'Y', 'X'],
    'Value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)
# Creating a pivot table
pivot_df = df.pivot_table(values='Value', index='Category', columns='Subcategory', aggfunc='sum')
print(pivot_df)

# Using pivot for reshaping
pivot_reshaped = df.pivot(index='Category', columns='Subcategory', values='Value')
print(pivot_reshaped)
```

**4. Grouping and Sorting**

Working with grouped data is essential when there's a need to summarize
information based on categorical variables. In this segment, Pandas\'
powerful **groupby()** function is introduced. It enables grouping rows
of data that share a common value in a particular column, making it
easier to apply aggregation functions like sum(), count(), or mean() on
these groups.

Additionally, the course covers how to sort data either by index or by
column values using the sort_values() and sort_index() methods. This
feature becomes especially useful when dealing with time series or any
scenario where the order of data is critical for analysis​
```python 
# Apply a custom aggregation function
def custom_agg(x):
    return x.sum() - x.min()

custom_group = df.groupby('Category')['Value'].apply(custom_agg)

# Filter groups by condition
filtered_group = df.groupby('Category').filter(lambda x: x['Value'].mean() > 25)
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})

# SQL-style merge on the 'key' column
merged_df = pd.merge(df1, df2, on='key', how='inner')
# Joining two DataFrames on index
df4 = pd.DataFrame({
    'value2': [10, 11]
}, index=['A', 'B'])

joined_df = df1.join(df4)
print(joined_df)
```

**5. Data Types and Missing Values**

Handling missing values is a critical aspect of data cleaning. This
section of the course dives into how Pandas deals with missing data
using methods like dropna() to remove missing values and fillna() to
replace them with substitute values. The replace() function is also
introduced for altering or imputing values in a DataFrame.

Moreover, ensuring that data is in the correct format is important for
accurate analysis. Pandas allows for easy conversion of data types using
astype(), ensuring that numerical, categorical, or datetime data are
handled appropriately based on the context of the analysis​
```python
# Sample data with missing values
data = {
    'Category': ['A', 'B', 'C', None, 'E'],
    'Value': [10, None, 30, 40, None]
}

df = pd.DataFrame(data)

# Check for missing values
print(df.isna())

# Fill missing values with a constant value (e.g., 0)
df_filled = df.fillna(0)
print(df_filled)

# Drop rows with any missing values
df_dropped = df.dropna()
print(df_dropped)

# Drop columns with any missing values
df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)
df_no_duplicates = df.drop_duplicates()
# Sorting by index
df_sorted_index = df.sort_index(ascending=False)

# Sorting by values (e.g., 'Value' column)
df_sorted_values = df.sort_values(by='Value', ascending=False)

```

**6. Renaming and Combining Data**

Data often comes from multiple sources, and combining datasets is a
common task in data analysis. The course covers how to **rename**
columns or rows using rename(), ensuring that datasets maintain clarity
and relevance.
```python
# Renaming columns
df_renamed_columns = df.rename(columns={'Category': 'Type', 'Value': 'Amount'})
print(df_renamed_columns)

# Renaming index
df_renamed_index = df.rename(index={0: 'row1', 1: 'row2', 2: 'row3', 3: 'row4', 4: 'row5'})
print(df_renamed_index)

```

**Combining data** through merging or concatenating multiple DataFrames
is also covered in detail. The concat() function enables appending one
DataFrame to another either vertically or horizontally. Meanwhile, the
merge() function is analogous to SQL joins, allowing for the combination
of DataFrames based on shared keys or columns. This is especially useful
for integrating multiple datasets into a single cohesive structure​



