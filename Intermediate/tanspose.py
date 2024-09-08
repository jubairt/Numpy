
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
