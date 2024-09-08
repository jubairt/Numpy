import numpy as np

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