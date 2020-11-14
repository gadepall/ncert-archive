import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#def destroy(self):
	#self.close_event()


#coodinates of vertices
A = np.array([-4,5])
B = np.array([0,7])
C = np.array([5,-5])
D = np.array([-4,-2]

#Calculating Area
Area=0.5*(np.cross(A-B,A-D)+np.cross(C-B,C-D))

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.03), B[1] * (1 + 0.1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.1), C[1] * (1 + 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.13), D[1] * (1 - 0.13) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('./pyfigs/quad.eps')

plt.show()
print("Area of triangle is ")
print(Area)	     

#print(5)

