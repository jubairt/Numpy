import numpy as np

# Converting 1D array to 2D array
n=np.array([1,2,3,4,5,6,7,8,9])
print(n)

reshaped=n.reshape(3,3)

print("\n")
print(reshaped)

# Coverting 3D array to 1D array
n=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
reshaped=n.reshape(-1)
print("\n")
print(reshaped)