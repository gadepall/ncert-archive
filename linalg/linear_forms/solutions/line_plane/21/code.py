#! /usr/bin/python3
import numpy as np
k = 2
a1 = 2*k-1
a2 = k-1
a3 = 2*k+1
a = np.array([[3,1],
            [a1,a2]])                  #Coefficient matrix
b = np.array([[1],[a3]])
c = np.concatenate((a,b), axis=1)      #Augmented matrix
#The linear equations will have no solution if rank(Coefficient matrix) is not equal to rank(Augmented matrix)
if np.linalg.matrix_rank(a) != np.linalg.matrix_rank(c):
    print("No solution for k =",k)