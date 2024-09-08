import numpy as np

n1=np.array([[[1,2,3],[4,5,6]],
             [[43,54,65],[87,65,56]]
             ])

print(n1[0,1,1])
print(n1[0,1])


# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing rows and columns
print("Rows 1 and 2, columns 1 and 2:")
print(array_2d[1:3, 1:3])  # Output: [[5 6]
                            #          [8 9]]
                            
                            
                            
# Create an array
array = np.array([10, 20, 30, 40, 50])

# Boolean indexing
condition = array > 30
print("Elements greater than 30:", array[condition])  # Output: [40 50]
