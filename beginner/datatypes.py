import numpy as np


# int data type
n=np.array([1,2,3])
print(n.dtype)

# String data type( unicode string )
n=np.array(["jubair","jaseela","jabit"])
print(n.dtype)

# String data type(explicitly)
n=np.array(["hello","hi","fine","where"],dtype='S9')
print(n.dtype)
print(n)



# Convert data type
n=np.array(["12","34","65","78"])
n2=n.astype('i')
print(n.dtype)
print(n2.dtype)
