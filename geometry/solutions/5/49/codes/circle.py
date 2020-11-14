
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#def destroy(self):
	#self.close_event()


#given input parameters
r = 4
len = 100
alpha= 2/3*np.pi
beta= 1/3*np.pi
#<EOC = <DOA = delta
delta= np.pi-(alpha+beta)/2


#coodinates of different points
O = np.array([0,0])
#B = np.array([5,-1])
A = np.array([r*np.cos(beta),-1*r*np.sin(beta)])
C = np.array([r,0])
D = np.array([r*np.cos(alpha+delta),r*np.sin(alpha+delta)])
E = np.array([r*np.cos(delta),r*np.sin(delta)])
Em=(E+C)/2
Dm=(D+A)/2

#Finding B
k=np.linalg.norm(C-E-A+D)/np.linalg.norm(A-C)
B=((k+1)*A-D)/k
print(B)

#Generating the circle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T

#plotting circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

#Generating all lines
x_DB = line_gen(D,B)
x_EB = line_gen(E,B)
x_OE = line_gen(O,E)
x_OC = line_gen(O,C)
x_OD = line_gen(O,D)
x_OA = line_gen(O,A)


#Plotting all lines
plt.plot(x_DB[0,:],x_DB[1,:],label='$BD$')
plt.plot(x_EB[0,:],x_EB[1,:],label='$EB$')
plt.plot(x_OE[0,:],x_OE[1,:],label='$OE$')
plt.plot(x_OC[0,:],x_OC[1,:],label='$OC$')
plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$')
plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.03), B[1] * (1 + 0.1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.1), C[1] * (1 + 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.13), D[1] * (1 - 0.13) , 'D')
#print(1)
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 +0.1), E[1] * (1 + 0.1) , 'E')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 +0.1), O[1] * (1 + 0.1) , 'O')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('./pyfigs/circle.eps')

plt.show()


#print(5)

