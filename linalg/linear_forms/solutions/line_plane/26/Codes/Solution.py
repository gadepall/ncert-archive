import numpy as np

def is_null_mat(A):
  '''
  Utility function to check if a matrix is null matrix
  '''
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      if (A[i,j]!=0):
        return False
  return True

A = np.array([[1,0,2],[0,2,1],[2,0,3]])
I = np.array([[1,0,0],[0,1,0],[0,0,1]])

# Computing A^2
A_2 = np.matmul(A,A)

# Computing A^2(A-6I)
C1 = np.matmul(A_2,A-6*I)

# Computing 7A+2I
C2 = 7*A+2*I

# Computing A^2(A-6I) + 7A+2I
Res = C1+C2
print("A^2(A-6I) + 7A+2I = \n",Res)

# Checking if the Res=A^2(A-6I) + 7A+2I is Null Matrix
if (is_null_mat(Res)==True):
  print('Result = Null Matrix, Proved')
else:
  print('Result != Null Matrix')
