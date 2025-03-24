# Report on Learning NumPy

**NumPy** is an essential library for numerical computing in Python,
offering robust data structures and efficient computation methods. After
completing the course, several core concepts were explored, and these
have significantly enhanced my understanding of how to handle numerical
data efficiently in Python. Below is a detailed overview of the key
subtopics covered in the course.

**1. Arrays and Array Creation**

The backbone of NumPy is the ndarray object. Arrays allow for fast,
memory-efficient storage of data, particularly numerical data. NumPy
arrays support element-wise operations and are highly optimized compared
to traditional Python lists.

- Arrays can be created using various functions such as numpy.array(),
  numpy.zeros(), numpy.ones(), and numpy.arange().

- You can also generate random arrays using numpy.random, which is
  useful for simulations and testing.
  
## Implement:
```python
# Creating arrays using different methods
array_from_list = np.array([1, 2, 3, 4, 5])  # From a Python list
array_of_zeros = np.zeros((3, 3))             # Array of zeros
array_of_ones = np.ones((2, 4))              # Array of ones
array_empty = np.empty((2, 2))               # Array with uninitialized values
array_with_arange = np.arange(0, 10, 2)      # Values from 0 to 10 with a step of 2
array_with_linspace = np.linspace(0, 1, 5)   # 5 evenly spaced values from 0 to 1
```
```python
# dtype defines the type of elements in the array
array_int = np.array([1, 2, 3], dtype=np.int32)   # Integer type array
array_float = np.array([1.1, 2.2, 3.3], dtype=np.float64)  # Float type array
array_bool = np.array([1, 0, 1], dtype=np.bool_)  # Boolean type array
```
**2. Array Indexing and Slicing**

Just like lists in Python, NumPy arrays support indexing and slicing,
but with added capabilities. This allows for easy extraction and
manipulation of array subsets.

- Negative indexing, boolean indexing, and advanced slicing provide
  flexible ways to retrieve and alter array data.

- Multi-dimensional arrays can be sliced along different axes, enabling
  manipulation of 2D or 3D data arrays with ease.

## Implement
```python
array = np.arange(10)  # Array from 0 to 9
slice1 = array[2:7]   # Elements from index 2 to 6
slice2 = array[:5]    # First 5 elements
slice3 = array[5:]    # Elements from index 5 to the end
slice4 = array[::2]   # Every second element
```
```python
# Applying a boolean condition
bool_condition = array_bool > 5  # Elements greater than 5
filtered_array = array_bool[bool_condition]
# Selecting specific indices
indices = [0, 2, 4]  # Selecting elements at index 0, 2, and 4
fancy_indexed_array = array_fancy[indices]
# Using fancy indexing with negative indices
negative_indices = [-1, -3, -5]  # Selecting last, third-last, and fifth-last elements
fancy_indexed_neg = array_fancy[negative_indices]
```

**3. Array Operations and Broadcasting**

One of NumPy's strengths is its ability to perform element-wise
operations and apply mathematical functions efficiently across entire
arrays without loops. This is known as **vectorization**.

- Vectorized operations include addition, subtraction, multiplication,
  division, and more.
- **Broadcasting** allows arrays of different shapes to be used together
  in operations, by expanding the smaller array across the larger one.
  This leads to more concise and readable code.

## Implement
```python
add_result = array1 + array2
mul_result = array1 * array2
div_result = array1 / array2
# 2. Broadcasting
array3 = np.array([1, 2, 3])
array4 = np.array([[10], [20], [30]])  # Broadcasting 1D to 2D
broadcast_result = array3 + array4

# 4. Linear Algebra Operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Dot product and matrix multiplication
dot_result = np.dot(matrix1, matrix2)
matmul_result = np.matmul(matrix1, matrix2)

# Matrix inverse and eigenvalues/eigenvectors
matrix3 = np.array([[2, 1], [1, 3]])
inv_result = np.linalg.inv(matrix3)
eig_values, eig_vectors = np.linalg.eig(matrix3)
```
```python
# Horizontal stacking
hstack_result = np.hstack((array1, array2))

# Vertical stacking
vstack_result = np.vstack((array1, array2))

# Splitting arrays
array_to_split = np.array([10, 20, 30, 40, 50, 60])
split_result = np.split(array_to_split, 3)  # Splitting into 3 equal parts
```
**4. Aggregation and Statistical Functions**

NumPy includes a wide range of mathematical functions that can be
applied across arrays, making it easy to compute statistical measures
and perform data analysis.

- Functions like numpy.mean(), numpy.median(), numpy.std(), and
  numpy.sum() are essential for summarizing data.

- Aggregation over specified axes of multi-dimensional arrays (e.g.,
  row-wise or column-wise) can be done using parameters like axis=0 or
  axis=1.

```python
# Sum, mean, max, and min
sum_result = np.sum(array5)
mean_result = np.mean(array5)
max_result = np.max(array5)
min_result = np.min(array5)
sum_axis_0 = np.sum(array5, axis=0)  # Sum along columns
sum_axis_1 = np.sum(array5, axis=1)  # Sum along rows
```
**5. Linear Algebra and Matrix Operations**

NumPy includes a dedicated submodule, numpy.linalg, for performing
various linear algebra operations, such as matrix multiplication,
inverses, and eigenvalues.

- Functions like numpy.dot() and numpy.matmul() enable efficient matrix
  operations.

- NumPy arrays can be used to represent vectors and matrices, and
  operations such as solving linear equations are streamlined.

```python
# Transpose using the T attribute
transposed_matrix = matrix.T
print("Transposed matrix:\n", transposed_matrix)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Dot product
dot_product = np.dot(matrix1, matrix2)
# 2. Using numpy.matmul() for Matrix Multiplication
matmul_result = np.matmul(matrix1, matrix2)
# 3. Solving Linear Equations
# Representing the system of equations:
# 2x + y = 5
# x + 3y = 7
A = np.array([[2, 1], [1, 3]])  # Coefficient matrix
B = np.array([5, 7])            # Constants vector

# Solving for x and y
solution = np.linalg.solve(A, B)
print("Coefficient matrix (A):\n", A)
print("Constants vector (B):", B)
print("Solution to the system of equations (x, y):", solution)

```
**6. Shape Manipulation**

Reshaping arrays is a common task when preparing data for machine
learning or statistical analysis. NumPy offers various functions for
altering array shapes without changing the underlying data.

- Functions such as numpy.reshape(), numpy.ravel(), and
  numpy.transpose() allow you to modify the structure of an array to fit
  specific needs.

```python
# Checking the shape and dimensions of arrays
print("Shape of array_of_zeros:", array_of_zeros.shape)
print("Number of dimensions (ndim) of array_of_zeros:", array_of_zeros.ndim)

# Reshaping arrays
array_to_reshape = np.arange(12)  # Array with 12 elements
reshaped_array = array_to_reshape.reshape(3, 4)  # Reshaping to 3 rows and 4 columns
print("Original array:", array_to_reshape)
print("Reshaped array (3x4):\n", reshaped_array)
```
**7. Advanced Features:**

Additional advanced features of NumPy include:

- **Memory-efficient views**: Modifying one part of an array may affect
  others because NumPy avoids copying data when possible.

- **Fancy Indexing**: A powerful tool that allows advanced operations on
  array subsets using lists or arrays as indices.

**8. Integration with Other Libraries**

NumPy serves as the foundation for many other Python libraries,
particularly in data science and machine learning, such as **Pandas**
and **Scikit-learn**. A solid understanding of NumPy lays the groundwork
for mastering these more advanced libraries.