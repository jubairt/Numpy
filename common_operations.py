# Joining arrays

import numpy as np

n1=np.array([1,2,3,4,5])
n2=np.array([0,2,3,4,5])

# Concatenate method
joined=np.concatenate((n1,n2))
print(joined)

# stack method, It will join in stack based
print("\n")
joined=np.stack((n1,n2),axis=1)
print(joined)

# hstack method, It will join along rows
print("\n")
joined=np.hstack((n1,n2))
print(joined)

# vstack method, It will join along columns
print("\n")
joined=np.vstack((n1,n2))
print(joined)

# dstack method, It will join along depth(height)
print("\n")
joined=np.dstack((n1,n2))
print(joined)

# column_stack method, It will join along column
print("\n")
joined=np.column_stack((n1,n2))
print(joined)


# ==============================================================
from numpy import random
# Random Generation

# this will display any one number from 0 to 5
n1=random.randint(5)
print(n1)

# this will display any 3 numbers from 0 to 5 as an array
n2=random.randint(5,size=3)
print(n2)

# by this choice method, it will only generate values that we gave as choice
n3=random.choice([45,7,54,34,23,54,67,34,23])
print(n3)

# ===================================================================

# Reshaping

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


# ===================================================================

# Shape of Arrays

# zero dimensional array
n=np.array(54)
print(n.ndim)
print(n.shape)

# One dimension
n=np.array([1,2,3])
print("Dimension=",n.ndim)
print(n.shape)

# Two dimension
n=np.array([[1,2,3],[4,5,6]])
print("Dimension=",n.ndim)
print(n.shape)

# Three dimension
n=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[1,2,3],[4,5,6]]])
print("Dimension=",n.ndim)
print(n.shape)


# ===================================================================
# ===================================================================