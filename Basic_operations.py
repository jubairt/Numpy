
import numpy as np

# Original array
array = np.array([1, 2, 3])

# Append a new element
array = np.append(array, 4)
print("Updated Array:", array)  # Output: [1 2 3 4]




# -------------------------------------

# Original array
array = np.array([1, 2, 3])

# New elements to add
new_elements = np.array([4, 5])

# Concatenate arrays
array = np.concatenate((array, new_elements))
print("Updated Array:", array)  # Output: [1 2 3 4 5]

# -------------------------------------

# Original array
array = np.array([1, 2, 3])

# Insert a new element at index 1
array = np.insert(array, 1, 4)
print("Updated Array:", array)  # Output: [1 4 2 3]



# ======================================================================
#Dimensions

# zero dimension
n=np.array(34)
print(n)
print("Dimension=",n.ndim)

# One dimension
n=np.array([1,2,3])
print(n)
print("Dimension=",n.ndim)

# Two dimension
n=np.array([[1,2,3],[4,5,6]])
print(n)
print("Dimension=",n.ndim)

# Three dimension
n=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[1,2,3],[4,5,6]]])
print(n)
print("Dimension=",n.ndim)

# -------------------

# Dimenstion expanding and squeezing

# Original 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("Original 1D array:")
print(array_1d)
print("Shape:", array_1d.shape)

# Output:
# Original 1D array:
# [1 2 3 4 5]
# Shape: (5,)

# Add a new axis to create a 2D array (axis=0)
expanded_array = np.expand_dims(array_1d, axis=0)
print("\nExpanded 2D array (new axis at position 0):")
print(expanded_array)
print("Shape:", expanded_array.shape)

# Output:
# Expanded 2D array (new axis at position 0):
# [[1 2 3 4 5]]
# Shape: (1, 5)

# Add a new axis to create a 2D array along the other dimension (axis=1)
expanded_array = np.expand_dims(array_1d, axis=1)
print("\nExpanded 2D array (new axis at position 1):")
print(expanded_array)
print("Shape:", expanded_array.shape)

# Output:
# Expanded 2D array (new axis at position 1):
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]]
# Shape: (5, 1)

# Create a 3D array with one dimension of size 1
array_3d = np.array([[[1, 2, 3], [4, 5, 6]]])
print("\nOriginal 3D array:")
print(array_3d)
print("Shape:", array_3d.shape)

# Output:
# Original 3D array:
# [[[1 2 3]
#   [4 5 6]]]
# Shape: (1, 2, 3)

# Remove single-dimensional entries
squeezed_array = np.squeeze(array_3d)
print("\nSqueezed array:")
print(squeezed_array)
print("Shape:", squeezed_array.shape)

# Output:
# Squeezed array:
# [[1 2 3]
#  [4 5 6]]
# Shape: (2, 3)




# expand_dims(): Use it to add new dimensions to an array.
# squeeze(): Use it to remove dimensions of size 1 from an array.


# ====================================================================================
# Basic Arithematics

n1=np.array([1,2,70,7])
n2=np.array([70,4,5,7])

# sum: will sum two arrays
summed=np.sum([n1,n2])
print(summed)

# row sum
summed=np.sum([n1,n2],axis=0)
print(summed)

# column sum
summed=np.sum([n1,n2],axis=1)
print(summed)

# subtract
subtracted=np.subtract(n1,n2)
print(subtracted)

# multiplication
multiplicated=np.multiply(n1,n2)
print(multiplicated)

# divide
divided=np.divide(n1,n2)
print(divided)

# ==========================================================================
# Data Types

# int data type
n=np.array([1,2,3])
print(n.dtype)

# String data type( unicode string )
n=np.array(["jubair","jaseela","jabit"])
print(n.dtype)

# String data type(explicitly)
n=np.array(["hello","hi","fine","where"],dtype='S9')
print(n.dtype)
print(n)



# Convert data type
n=np.array(["12","34","65","78"])
n2=n.astype('i')
print(n.dtype)
print(n2.dtype)

# =================================================================
# Indexing and Slicing

n1=np.array([[[1,2,3],[4,5,6]],
             [[43,54,65],[87,65,56]]
             ])

print(n1[0,1,1])
print(n1[0,1])


# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing rows and columns
print("Rows 1 and 2, columns 1 and 2:")
print(array_2d[1:3, 1:3])  # Output: [[5 6]
                            #          [8 9]]
                            
                            
                            
# Create an array
array = np.array([10, 20, 30, 40, 50])

# Boolean indexing
condition = array > 30
print("Elements greater than 30:", array[condition])  # Output: [40 50]

# -------------------------

# 1. Boolean Indexing
# Boolean indexing allows you to select elements of an array using a boolean array of the same shape. Wherever the boolean array has True, the corresponding element from the original array is selected.

import numpy as np

# Create a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Create a boolean condition (select elements greater than 30)
condition = arr > 30

# Use boolean indexing
result = arr[condition]
print("Boolean Indexing Result:", result)
# Output: [40 50]


# Here, the condition arr > 30 creates a boolean array [False, False, False, True, True]. When applied to arr, only the elements at the True positions are selected.

# ---------------------------------------------------------------------------------------------------------

# 2. Fancy Indexing
# Fancy indexing allows you to use arrays of indices to access specific elements. You can select elements by their index positions in a flexible and powerful way.

# 1D Fancy Indexing Example:
import numpy as np

# Create a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Use fancy indexing to select elements at specific positions
indices = [0, 2, 4]
result = arr[indices]
print("Fancy Indexing Result:", result)
# Output: [10 30 50]


# 2D Fancy Indexing Example:
import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

# Use fancy indexing to select specific rows and columns
rows = [0, 2]
cols = [1, 2]

# arr[0, 1] = 2 (first row, second column)
# arr[2, 2] = 9 (third row, third column)

result = arr[rows, cols]
print("Fancy Indexing on 2D Array:", result)
# Output: [2 9]

# Here, rows = [0, 2] and cols = [1, 2] selects the elements at positions (0,1) and (2,2).

# ----------------------------------------------------------------------------------------------------------

# 3. Advanced Slicing

# 2D Slicing Example:
import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9], 
                [10, 11, 12]])

# Slice a submatrix (rows 1 to 3, columns 0 to 2)
result = arr[1:3, 0:2]
print("Advanced Slicing on 2D Array:")
print(result)
# Output:
# [[4 5]
#  [7 8]]

# Here, we sliced rows from index 1 to 3 (excluding index 3) and columns from index 0 to 2 (excluding index 2), extracting a submatrix.

# ----------------------------------------------------------------------------------------------------------

# Combining Indexing and Slicing
import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

# Boolean condition
condition = arr > 4

# Fancy indexing with slicing
rows = [1, 2]
cols = slice(1, 3)

# Apply boolean indexing followed by fancy slicing
result = arr[rows, cols][condition[rows, cols]]
print("Combined Indexing and Slicing Result:", result)
# Output: [5 6 8 9]

# Here, we first used boolean indexing to filter elements greater than 4, then applied fancy indexing and slicing to extract specific rows and columns.


# --------------------------------------------------------------------------------------------------------
# Modifying Arrays with Boolean Indexing

import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

# Modify elements greater than 5
arr[arr > 5] = 0

print("Modified 2D Array (Boolean Indexing):")
print(arr)
# Output:
# [[1 2 3]
#  [4 5 0]
#  [0 0 0]]

# ------------------

# 2. Modifying Arrays with Fancy Indexing

import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

# Modify elements at specific row and column positions
arr[[0, 2], [1, 2]] = [99, 88]

print("Modified 2D Array (Fancy Indexing):")
print(arr)
# Output:
# [[ 1 99  3]
#  [ 4  5  6]
#  [ 7  8 88]]

# ---------------------------

# 3. Modifying Arrays with Advanced Slicing

import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

# Modify a slice of the array (submatrix)
arr[1:3, 1:3] = [[99, 88], [77, 66]]

print("Modified 2D Array (Slicing):")
print(arr)
# Output:
# [[ 1  2  3]
#  [ 4 99 88]
#  [ 7 77 66]]

# ------------------

#  Combining Boolean Indexing and Slicing:

import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

# Create a condition to select elements in the first two rows greater than 2
arr[:2, :][arr[:2, :] > 2] = 99

print("Modified Array (Boolean Indexing and Slicing):")
print(arr)
# Output:
# [[ 1  2 99]
#  [99 99 99]
#  [ 7  8  9]]

# ================================================================================
# Array Initialization

# initialze ex1
n=np.zeros([2,3])# 2 rows and 3 columns
print(n)
print(type(n))


# initialze ex2
n=np.zeros([4,4])# 4 rows and 4 columns
print(n)
print(type(n))

# It will give one , instead of zero
n1=np.ones([2,3])
print(n1)

# This is like range() function, but it will give output of array instead of object
n1=np.arange(1,11).reshape(5,2)
print(n1)

n2=np.arange(10)
print(n2)

# -------------------------------------

# -------------------------------------


