import numpy as np

num1=3
num2=12


#  this will give lcm(least common multiple of two numbers)
# It means that both two number's least multiple that multiplication result should be included in both numbers
lcm=np.lcm(num1,num2)
print(lcm)


# GCD(greatest common divisor)=HCF(Heighest common factor) , it is the heighest factor or divisor included in both numbers

hiehest_factor=np.gcd(num1,num2)
print(hiehest_factor)
