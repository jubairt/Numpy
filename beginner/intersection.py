import numpy as np

n1=np.array([1,2,70,7])
n2=np.array([70,4,5,7])

# instersection finds its intersect and sort the values
intersected=np.intersect1d(n1,n2)
print(intersected)