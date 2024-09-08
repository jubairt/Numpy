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
