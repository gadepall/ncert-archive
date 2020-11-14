import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy import linalg as LA

A=np.matrix('3 1; 2 2; 6 2')
b=np.matrix('5; -1; -1')

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
print(Sinv)
#Moore-Penrose Pseudoinverse
Aplus = V.T.dot(Sinv).dot(U.T)
#Least squares solution
x_ls = Aplus.dot(b)
#
print(x_ls)
