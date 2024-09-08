import numpy as np

# initialze ex1
n=np.zeros([2,3])# 2 rows and 3 columns
print(n)
print(type(n))


# initialze ex2
n=np.zeros([4,4])# 4 rows and 4 columns
print(n)
print(type(n))

# It will give one , instead of zero
n1=np.ones([2,3])
print(n1)

# This is like range() function, but it will give output of array instead of object
n1=np.arange(1,11).reshape(5,2)
print(n1)

n2=np.arange(10)
print(n2)