import numpy as np


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

