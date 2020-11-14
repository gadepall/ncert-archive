import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy import linalg as LA

M=np.matrix('1 0; 0 1; -1 1.3333 ')
print(M)
b=np.matrix('6; 5; 9')
print(b)

#SVD, M=USV
U, s, V=LA.svd(M)
#Find size of M
mn=M.shape
#Creating the singular matrix
S = np.zeros(mn)

Sinv = S.T
S[:2,:2] = np.diag(s)

#Verifying the SVD, M=USV
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
