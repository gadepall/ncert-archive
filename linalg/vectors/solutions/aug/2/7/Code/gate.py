'''
Author: Chirag
EE3900
Assignment-1 Vectors
'''
import numpy as np
import matplotlib.pyplot as plt
from sympy.matrices import Matrix

#input points
A=np.array([1,5])
B=np.array([2,3])
C=np.array([-2,-11])

#printing input
print("A:\n ",A)
print("B:\n ",B)
print("C:\n ",C)

#Making the M matrix
M=Matrix([B-A,C-A])

# verifing M with what was calculated in tex file
print(M)

# taking rref of M matrix
M_rref = M.rref()
print("The reff of matrix M is given as : ",M_rref)

# Calculating the rank of Matrix M (here M and N respresent same matrix)
N=np.array([B-A,C-A])
print ("rank of matrix = ",np.linalg.matrix_rank(N))


#plotting the points
plt.plot(A[0], A[1], 'o')
plt.text(A[0], A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.05), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1+0.05), C[1] * (1 - 0.05) , 'C')
plt.plot(np.array([1,2]),np.array([5,3]), 'b', label="$AB$")
plt.plot(np.array([2,-2]), np.array([3,-11]),'r', label="$BC$")
plt.plot(np.array([1,-2]), np.array([5,-11]),'g', label="$CA$")
plt.grid()
plt.xlim(-3,3)
plt.ylim(-14,7)
plt.legend(loc='lower right')
plt.show()
