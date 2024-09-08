import numpy as np

n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("min value in axis=0 (vertical axis or row based) =", n.min(axis=0))
print("min value in axis=1 (Horizontal axis or column based) =", n.min(axis=1))