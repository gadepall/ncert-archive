import numpy as np

M = np.array([[1,0],[0,1],[-1/3,1/2]])
b = np.array([[-6],[0],[0]])

#Singular Value Decomposition
U, s, V=np.linalg.svd(M)

# Diagonalizing S
S = np.zeros(M.shape)
Sinv = S.T
S[:2,:2] = np.diag(s)
sinv = 1./s

#Inverse transpose of S (Moore Penrose Pseudo Inverse)
Sinv[:2,:2] = np.diag(sinv)

#Solution
x = V.T.dot(Sinv).dot(U.T).dot(b)
print(x)
