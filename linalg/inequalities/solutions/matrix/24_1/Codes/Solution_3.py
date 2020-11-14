import numpy as np
def MatMul(A,B):
  '''
  A function for matrix multiplication
  '''
  if (A.shape[1]!=B.shape[0]):
    return "Matrix Multiplication not possible due to shape mismatch"
  shape_A = A.shape[0]
  shape_B = B.shape[1]
  result = np.zeros(shape = (shape_A,shape_B),dtype = int)
  for i in range(shape_A):
    for j in range(shape_B):
      for k in range(A.shape[1]): 
        result[i,j] += A[i,k]*B[k,j]
  return result

def isequal(A,B):
  '''
  Program to check if two matrices are equal
  '''
  if A.shape!=B.shape:
    return False
  else:
    for i in range(A.shape[0]):
      for j in range(A.shape[1]):
        if (A[i,j]!=B[i,j]):
          return False
  return True

# Defining the matrices
a = np.array([[5,-1],[6,7]])
b = np.array([[2,1],[3,4]])

# Calculating the products
ab = MatMul(a,b)
ba = MatMul(b,a)

'''
Alternatively: Use Numpy builtin numpy.matmul function
ab = np.matmul(a,b)
ba = np.matmul(b,a)
'''
# Decision
if (isequal(ab,ba)):
  print("AB = BA")
else:
  print("AB != BA")
