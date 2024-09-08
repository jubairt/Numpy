import numpy as np

n1=np.array([1,2,70,7])
n2=np.array([70,4,5,7])

# setdiff will remove common elements from both arrays and display the rest of the elements from the first array
differenced=np.setdiff1d(n1,n2)
print(differenced)