import numpy as np

A=np.array([(1,3,-2),(-3,0,-5),(2,5,0)])
print("Matrix A is as follows:")
print(A)
print("The inverse of matrix A is as follows")
print(np.linalg.inv(A))