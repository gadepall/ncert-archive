
## Author: Ganji Varshitha (AI20BTECH11009) ##
## Code to plot the points after finding the value of unknown and check whether they are collinear ##
#importing numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

### (1) A=(7,-2) B=(5,1) C=(3,k) 
### k=4 so A=(7,-2) B=(5,1) C=(3,4)
#Defining the points A,B,C
A = np.array([7,-2]) 
B = np.array([5,1]) 
C = np.array([3,4]) 
#Making the matrix M=transpose of (B-A C-A)
M=np.vstack((B-A,C-A))
#Calculating the rank of matrix M
rank=np.linalg.matrix_rank(N)
print('Matrix M is: ',M)
print('Rank of M is: ',rank)

#plotting the points
plt.plot(A[0], A[1], 'o')
plt.text(A[0], A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.05), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1+0.05), C[1] * (1 - 0.05) , 'C')
plt.plot(np.array([7,5]),np.array([-2,1]), 'b', label="$AB$")
plt.plot(np.array([5,3]), np.array([1,4]),'r', label="$BC$")
plt.plot(np.array([7,3]), np.array([-2,4]),'g', label="$CA$")
plt.grid()
plt.xlim(-2,10)
plt.ylim(-4,5)
plt.legend(loc='lower right')
plt.show()

### (2) A=(8,1) B=(k,-4) C=(2,5) 
### k=3 so A=(8,1) B=(3,-4) C=(2,5)
#Defining the points A,B,C
A = np.array([8,1]) 
B = np.array([3,-4]) 
C = np.array([2,-5]) 
#Making the matrix M=transpose of (B-A C-A)
M=np.vstack((B-A,C-A))
#Calculating the rank of matrix M
rank=np.linalg.matrix_rank(N)
print('Matrix M is: ',M)
print('Rank of M is: ',rank)

#plotting the points
plt.plot(A[0], A[1], 'o')
plt.text(A[0], A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.05), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1+0.05), C[1] * (1 - 0.05) , 'C')
plt.plot(np.array([8,3]),np.array([1,-4]), 'b', label="$AB$")
plt.plot(np.array([3,2]), np.array([-4,-5]),'r', label="$BC$")
plt.plot(np.array([8,2]), np.array([1,-5]),'g', label="$CA$")
plt.grid()
plt.xlim(-6,10)
plt.ylim(-6,7)
plt.legend(loc='lower right')
plt.show()

