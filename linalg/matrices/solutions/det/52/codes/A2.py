import numpy as np
from numpy import newaxis
import matplotlib.pyplot as plt
from coeffs import *


#Lines
l1 = np.array([1,2]) 
l2 = np.array([2,3]) 
B =  np.array([2,3])

# Lines in Matrix equation Ax=B and G as Augmented matrix
A=np.vstack((l1,l2))
G=np.column_stack((A,B[:,newaxis]))

# Checking the consistency of the system of equations
Rank_A=np.linalg.matrix_rank(A)
#print(Rank_A)
Rank_G=np.linalg.matrix_rank(G)
#print(Rank_G)
#Dimension of matrix A n rows and m columns
(n,m)=np.shape(A)
#print(n,m)

if Rank_A==Rank_G:
	if Rank_A == n:
		print("System is consistent and has unique solution:",np.linalg.inv(A)@B)
	else:
		print("System has infinite solutions")
else:
	print("System of equations id inconsistent")

#intersection point
X=np.linalg.inv(A)@B

#Points on the lines AB and CD
A=np.array([4,3]).reshape((2,1))
B=np.array([0,-5]).reshape((2,1))
C=np.array([4,0]).reshape((2,1))
D=np.array([0,4]).reshape((2,1))

#Generating the lines
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Plotting the lines
plt.plot(x_AB[0,:],x_AB[1,:],label="x+2y=2")
plt.plot(x_CD[0,:],x_CD[1,:],label="2x+3y=3")


#plotting point
ax.scatter(X[0],X[1],marker='o')
ax.text(3,1,0, "X(0,1,0)", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()