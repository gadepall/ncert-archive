import numpy as np
x=np.array([[1,0,-1,0,0],[2,0,0,-1,0],[0,2,0,-1,0],[0,-1,-1,0,0],[1,4,-4,0,0]])
m,n=5,5
mat_2=x 
E_matrix=np.identity(m)    #Elimination matrix initialisation
print("Matrix that you have entered is :\n",mat_2)
for k in range(n-1):
  I1=np.identity(m,dtype=float) 
  if mat_2[k][k]==0:
    I2=np.identity(m,dtype=float)
    I2[[k,k+1]]=I2[[k+1,k]]        # This creates a Permutation matrix by swapping the rows of identity matrix.
    mat_2 = I2 @ mat_2            
  I1[k+1:m,k]=mat_2[k+1:m,k]/(-mat_2[k][k]) # This creates the Elimination matrix   
  E_matrix= I1 @ E_matrix          # This gives the repeated product of elimination matrices.
  mat_2 = I1 @ mat_2        # This performs the row tranformations on mat_2 and finally give reduced row echelon form of matrix.

print("Row reduced echelon form of your matrix is :\n",mat_2)

#OUTPUT: 
"""Matrix that you have entered is :
 [[ 1  0 -1  0  0]
 [ 2  0  0 -1  0]
 [ 0  2  0 -1  0]
 [ 0 -1 -1  0  0]
 [ 1  4 -4  0  0]]
Row reduced echelon form of your matrix is :
 [[ 1.  0. -1.  0.  0.]
 [ 0.  2.  0. -1.  0.]
 [ 0.  0.  2. -1.  0.]
 [ 0.  0.  0. -1.  0.]
 [ 0.  0.  0.  0.  0.]]"""
