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

# ---------------------------------------------------------------------------------------
