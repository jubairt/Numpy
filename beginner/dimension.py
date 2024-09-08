import numpy as np


# zero dimension
n=np.array(34)
print(n)
print("Dimension=",n.ndim)

# One dimension
n=np.array([1,2,3])
print(n)
print("Dimension=",n.ndim)

# Two dimension
n=np.array([[1,2,3],[4,5,6]])
print(n)
print("Dimension=",n.ndim)

# Three dimension
n=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[1,2,3],[4,5,6]]])
print(n)
print("Dimension=",n.ndim)

