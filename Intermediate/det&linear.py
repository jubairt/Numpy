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

# ---------------------------------------------------------------------------------

