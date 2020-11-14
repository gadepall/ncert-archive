#Code by GVV Sharma
#March 26, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *



#Triangle vertices
A = np.array([0,3,0]) 
B = np.array([0,-1,0]) 
C = np.array([2,1,0]) 

#Midpoints
D= np.add(A,B)/2
E=np.add(B,C)/2
F= np.add(A,C)/2

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_DE = line_gen(D,E)
x_EF = line_gen(E,F)
x_FD = line_gen(F,D)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')
plt.plot(x_FD[0,:],x_FD[1,:],label='$FD$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 - 0.2), E[1] * (1) , 'E')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

plt.show()






