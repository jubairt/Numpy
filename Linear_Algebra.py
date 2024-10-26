# Determinants and Solving System of equations


# 3. Computing Determinants
# The determinant of a square matrix can be computed using np.linalg.det().

# Determinants are Defined Only for Square Matrices
# A determinant is only defined for square matrices, which means the matrix must have the same number of rows and columns (like 2x2, 3x3, etc.). In your case, the matrix:

import numpy as np

# Create a 2D array (square matrix)
matrix = np.array([[1, 2], [3, 4]])

# Compute the determinant
determinant = np.linalg.det(matrix)
print("Determinant of the matrix:", determinant)
# Output: -2.0

# -----------------------------------------------------------------------------------------------

# 4. Solving Linear Equations
# To solve a system of linear equations Ax=b you can use np.linalg.solve(). Here,A is a matrix of coefficients, x is the vector of unknowns, and b is the vector of constants.

import numpy as np

# Coefficient matrix (A)
# it should be also square metrices
A = np.array([[3, 4], [2, 1]])

# Constant matrix (b)
b = np.array([10, 5])

# Solve the linear equations
solution = np.linalg.solve(A, b)
print("Solution to the linear equations:")
print(solution)
# Output: [2. 1.]

# In this example, the system of equations is:
# 3x+4y=10
# 2x+y=5
# the solution x=2 and y=1 satisfies both equations

# ==================================================================================
# Dot Product

# Dot Product of 1D Arrays:

import numpy as np

# 1-D Array = Vector
# 2-D Array = Matrix
# 3-D or Higher Array = Tensor

# Create two 1D arrays (vectors)
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Compute dot product
dot_product = np.dot(vector1, vector2)
print("Dot Product of 1D Arrays:", dot_product)
# Output: 32 (1*4 + 2*5 + 3*6)

# ---------------------------------------------------------------------------------------

# Matrix Multiplication with 2D Arrays:
import numpy as np

# Create two 2D arrays (matrices)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Compute matrix multiplication
matrix_product = np.dot(matrix1, matrix2)
print("Matrix Multiplication using np.dot():")
print(matrix_product)
# Output:
# [[19 22]
#  [43 50]]


# ==================================================================================
# Multiplication of Metrices

# Matrix Multiplication with 2D Arrays:

import numpy as np

# Create two 2D arrays (matrices)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Compute matrix multiplication
matrix_product = np.matmul(matrix1, matrix2)
print("Matrix Multiplication using np.matmul():")
print(matrix_product)
# Output:
# [[19 22]
#  [43 50]]


# ---------------------------------------------------------------------------------------

# Matrix and Vector Multiplication:
import numpy as np

# Create a matrix and a vector
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([7, 8, 9])

# Compute matrix-vector multiplication
result = np.matmul(matrix, vector)
print("Matrix-Vector Multiplication:")
print(result)
# Output: [50 122]

# ==================================================================================
# Transpose of Metrices


# 2. Transposing Matrices
# The transpose of a matrix swaps its rows and columns. In NumPy, this can be achieved using .T or np.transpose().

import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Transpose the matrix
transposed_matrix = matrix.T
print("Transposed Matrix using .T:")
print(transposed_matrix)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# ---------------------------------------------------------------------


import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Transpose the matrix
transposed_matrix = np.transpose(matrix)
print("Transposed Matrix using np.transpose():")
print(transposed_matrix)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# ==================================================================================
# ==================================================================================

