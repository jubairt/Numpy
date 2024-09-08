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
