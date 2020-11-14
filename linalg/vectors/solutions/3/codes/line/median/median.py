
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#def destroy(self):
	#self.close_event()
#VERTICES OF TRIANGLE
A = np.array([0,0])
B = np.array([2,2])
C = np.array([4,0])
#midponts of sides
D=(C+B)*1/2
E=(A+C)*1/2
F=(A+B)*1/2
#CENTROID
O=(2*D+A)*1/3

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_DA = line_gen(D,A)
x_EB = line_gen(E,B)
x_FC = line_gen(F,C)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')
plt.plot(x_EB[0,:],x_EB[1,:],label='$EB$')
plt.plot(x_FC[0,:],x_FC[1,:],label='$FC$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 +0.1), B[1] * (1 - 0.03) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.02), C[1] * (1 - 0.1) , 'C')

plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.02), E[1] * (1 - 0.1) , 'E')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.02), F[1] * (1 - 0.1) , 'F')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.02), D[1] * (1 - 0.1) , 'D')

plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
#plotting the lines
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

plt.savefig('./pyfigs/median.eps')

#print(3)
plt.show()
#print(4)



