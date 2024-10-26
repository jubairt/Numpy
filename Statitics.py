
import numpy as np

# Mean
n1=np.array([7,1,3,5,4,6,2])
mean_rslt=np.mean(n1)
print(mean_rslt)

# median
median_rslt=np.median(n1)
print(mean_rslt)

# standard deviation
# when all values are close to the mean, std would be small value or it would be large
std_ex1=np.array([4,3,5,4,3,5])
std_ex2=np.array([1,54,556,78])

std_made1=np.std(std_ex1)
std_made2=np.std(std_ex2)
print(std_made1)
print(std_made2)

# ----------------------------------------------------------------------------------------------

import numpy as np

# Example 1: Variance of a 1D array
data = np.array([10, 12, 23, 23, 16, 23, 21, 16])

# Compute the population variance of the 1D array
variance = np.var(data)

print("Variance of the 1D data:", variance)
# Output: Variance of the 1D data: 19.359375

# Example 2: Variance along axes in a 2D array
data_2d = np.array([[10, 12, 23],
                    [23, 16, 23],
                    [21, 16, 15]])

# Compute the variance along axis 0 (column-wise)
variance_col = np.var(data_2d, axis=0)

# Compute the variance along axis 1 (row-wise)
variance_row = np.var(data_2d, axis=1)

print("Column-wise variance:", variance_col)
# Output: Column-wise variance: [24.22222222  4.22222222 13.55555556]

print("Row-wise variance:", variance_row)
# Output: Row-wise variance: [30.88888889  8.22222222  6.22222222]

# Example 3: Population vs Sample Variance
# Population variance
population_variance = np.var(data)

# Sample variance with ddof=1 (Delta degrees of freedom)
sample_variance = np.var(data, ddof=1)

print("Population Variance:", population_variance)
# Output: Population Variance: 19.359375

print("Sample Variance:", sample_variance)
# Output: Sample Variance: 22.125


# =====================================================================

# LCM and HCF
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

# =================================================================

# Log operation

n=np.array([1,2,34,5,6,76])


# This will give all the log2 values (log 2 base)
logged=np.log2(n)
print(logged)

# This will give all the log10 values (log 10 base)
logged=np.log10(n)
print(logged)

# ==============================================================

# Removing common elements

n1=np.array([1,2,70,7])
n2=np.array([70,4,5,7])

# setdiff will remove common elements from both arrays and display the rest of the elements from the first array
differenced=np.setdiff1d(n1,n2)
print(differenced)

# ==============================================================