import numpy as np

n1=np.array([1,2,70,7])
n2=np.array([70,4,5,7])

# sum: will sum two arrays
summed=np.sum([n1,n2])
print(summed)

# row sum
summed=np.sum([n1,n2],axis=0)
print(summed)

# column sum
summed=np.sum([n1,n2],axis=1)
print(summed)

# subtract
subtracted=np.subtract(n1,n2)
print(subtracted)

# multiplication
multiplicated=np.multiply(n1,n2)
print(multiplicated)

# divide
divided=np.divide(n1,n2)
print(divided)