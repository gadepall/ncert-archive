#Code by GVV Sharma
#March 26, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


def tri_coord(a,b,c):
	p = (a**2 + c**2-b**2 )/(2*a)
	q = np.sqrt(c**2-p**2)
	A = np.array([p,q]) 
	return A

#Quadrilateral vertices
A = np.array([-1,2]) 
C = np.array([3,2]) 
e= np.linalg.norm(A-C)
B= np.array([1,0])
D=np.array([1,4])
E= np.add(A,C)/2


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(A,C)
x_DA = line_gen(D,A)
x_CD = line_gen(C,D)
x_BD = line_gen(B,D)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E')

plt.axis("equal")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

plt.show()







