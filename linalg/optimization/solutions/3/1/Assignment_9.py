
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy import linalg as LA

A=np.matrix('2 3; -1 -5; 1 2')
print(A)
b=np.matrix('1; 0; -1')
print(b)

#SVD, A=USV
U, s, V=LA.svd(A)
#Find size of A
mn=A.shape
#Creating the singular matrix
S = np.zeros(mn)

Sinv = S.T
S[:2,:2] = np.diag(s)

#Verifying the SVD, A=USV
print(U.dot(S).dot(V))
#Inverting s
sinv = 1./s
#Inverse transpose of S
Sinv[:2,:2] = np.diag(sinv)

#Moore-Penrose Pseudoinverse
Aplus = V.T.dot(Sinv).dot(U.T)
#Least squares solution
x_ls = Aplus.dot(b)
#
print(x_ls)