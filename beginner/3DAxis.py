import numpy as np

n1=np.array([[[56,2,7],
              [4,67,34]],
             
             [[4,65,2],
              [90,56,3]]])
n2=np.array([2,3,4])


print(np.min(n1,axis=1))