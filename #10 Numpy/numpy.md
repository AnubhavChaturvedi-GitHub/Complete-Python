# NumPy Project

## Overview

This project demonstrates the use of NumPy, a fundamental package for scientific computing with Python. NumPy provides support for arrays, matrices, and numerous mathematical functions to operate on these data structures efficiently.

## Features

- Creation of arrays
- Array indexing and slicing
- Mathematical operations
- Statistical operations
- Linear algebra operations
- Random number generation
- Reshaping and broadcasting

## Installation

To use NumPy, you need to install it using pip. If you haven't installed NumPy yet, you can do so by running:

```bash
pip install numpy
```

## Usage

### 1. Creating Arrays

```python
import numpy as np

# 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array (Matrix):\n", array_2d)

# Array with zeros
zeros_array = np.zeros((3, 3))
print("Array with Zeros:\n", zeros_array)

# Array with ones
ones_array = np.ones((2, 4))
print("Array with Ones:\n", ones_array)

# Identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)
```

**Output:**
```
1D Array: [1 2 3 4 5]
2D Array (Matrix):
 [[1 2 3]
  [4 5 6]]
Array with Zeros:
 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]
Array with Ones:
 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]]
Identity Matrix:
 [[1. 0. 0.]
  [0. 1. 0.]
  [0. 0. 1.]]
```

### 2. Array Indexing and Slicing

```python
# Indexing
element = array_2d[1, 2]
print("Element at row 1, column 2:", element)

# Slicing
slice_1d = array_1d[1:4]
print("Slice of 1D Array (index 1 to 3):", slice_1d)

slice_2d = array_2d[:, 1]
print("Second column of 2D Array:\n", slice_2d)
```

**Output:**
```
Element at row 1, column 2: 6
Slice of 1D Array (index 1 to 3): [2 3 4]
Second column of 2D Array:
 [2 5]
```

### 3. Mathematical Operations

```python
# Basic operations
sum_array = np.sum(array_1d)
print("Sum of 1D Array Elements:", sum_array)

mean_array = np.mean(array_1d)
print("Mean of 1D Array Elements:", mean_array)

std_dev_array = np.std(array_1d)
print("Standard Deviation of 1D Array Elements:", std_dev_array)

# Element-wise operations
addition = array_1d + 5
print("1D Array + 5:", addition)

multiplication = array_2d * 2
print("2D Array * 2:\n", multiplication)
```

**Output:**
```
Sum of 1D Array Elements: 15
Mean of 1D Array Elements: 3.0
Standard Deviation of 1D Array Elements: 1.4142135623730951
1D Array + 5: [ 6  7  8  9 10]
2D Array * 2:
 [[ 2  4  6]
  [ 8 10 12]]
```

### 4. Statistical Operations

```python
# Sum
total_sum = np.sum(array_2d)
print("Sum of 2D Array Elements:", total_sum)

# Mean
mean_value = np.mean(array_2d)
print("Mean of 2D Array Elements:", mean_value)

# Standard Deviation
std_dev = np.std(array_2d)
print("Standard Deviation of 2D Array Elements:", std_dev)
```

**Output:**
```
Sum of 2D Array Elements: 21
Mean of 2D Array Elements: 3.5
Standard Deviation of 2D Array Elements: 1.707825127659933
```

### 5. Linear Algebra Operations

```python
from numpy.linalg import inv, det, eig

# Matrix inversion
matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = inv(matrix)
print("Inverse of Matrix:\n", inverse_matrix)

# Determinant
determinant = det(matrix)
print("Determinant of Matrix:", determinant)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(matrix)
print("Eigenvalues of Matrix:", eigenvalues)
print("Eigenvectors of Matrix:\n", eigenvectors)
```

**Output:**
```
Inverse of Matrix:
 [[-2.   1. ]
  [ 1.5 -0.5]]
Determinant of Matrix: -2.0000000000000004
Eigenvalues of Matrix: [-0.37228132  5.37228132]
Eigenvectors of Matrix:
 [[-0.82456484 -0.41597356]
  [ 0.56576746 -0.90937671]]
```

### 6. Random Number Generation

```python
# Random integers
random_integers = np.random.randint(0, 10, size=(3, 3))
print("Random Integers:\n", random_integers)

# Random floats
random_floats = np.random.rand(2, 3)
print("Random Floats:\n", random_floats)

# Random normal distribution
normal_dist = np.random.randn(4, 4)
print("Random Normal Distribution:\n", normal_dist)
```

**Output:**
```
Random Integers:
 [[3 7 4]
  [8 1 5]
  [0 9 6]]
Random Floats:
 [[0.43559303 0.6887413  0.37341544]
  [0.18713022 0.66343082 0.04772836]]
Random Normal Distribution:
 [[ 0.43517952 -0.22010752  0.0724731  -0.04413258]
  [ 0.42561386 -0.02518942  1.29957288 -1.23457539]
  [-0.21134715 -1.29513046 -0.17073448 -0.39348766]
  [-1.16189002  0.34921972  0.15809828  0.14596757]]
```

### 7. Reshaping and Broadcasting

```python
# Reshaping
reshaped_array = np.reshape(array_1d, (5, 1))
print("Reshaped Array (5x1):\n", reshaped_array)

# Broadcasting
broadcasted_array = array_1d + np.array([[10], [20], [30], [40], [50]])
print("Broadcasted Array:\n", broadcasted_array)
```

**Output:**
```
Reshaped Array (5x1):
 [[1]
  [2]
  [3]
  [4]
  [5]]
Broadcasted Array:
 [[11 12 13 14 15]
  [21 22 23 24 25]
  [31 32 33 34 35]
  [41 42 43 44 45]
  [51 52 53 54 55]]
```

