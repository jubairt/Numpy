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
