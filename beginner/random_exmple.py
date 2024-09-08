from numpy import random

# this will display any one number from 0 to 5
n1=random.randint(5)
print(n1)

# this will display any 3 numbers from 0 to 5 as an array
n2=random.randint(5,size=3)
print(n2)

# by this choice method, it will only generate values that we gave as choice
n3=random.choice([45,7,54,34,23,54,67,34,23])
print(n3)