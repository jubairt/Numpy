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


