import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if

len = 100
r=2
#Generating the circle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
#x_circ = (x_circ.T + I).T
O = np.array([0,0])
A = np.array([r*np.cos(-3.14/4),r*np.sin(-3.14/4)])
B = np.array([r*np.cos(3.14/4),r*np.sin(3.14/4)])
X = np.array([1.414,0])


D = np.array([r*np.cos(-5*3.14/4),r*np.sin(-5*3.14/4)])
C= np.array([r*np.cos(5*3.14/4),r*np.sin(5*3.14/4)])
Y = np.array([-1.414,0])
#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.plot(r*np.cos(3.14/4),r*np.sin(3.14/4),'o')
plt.plot(r*np.cos(-3.14/4),r*np.sin(-3.14/4),'o')
plt.plot(1.414,0,'o')
plt.plot(0, 0, 'o')

plt.plot(r*np.cos(-5*3.14/4),r*np.sin(5*3.14/4),'o')
plt.plot(r*np.cos(-5*3.14/4),r*np.sin(-5*3.14/4),'o')
plt.plot(-1.414,0,'o')


x_AB = line_gen(A,B)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OX = line_gen(O,X)

x_CD = line_gen(C,D)
x_OC = line_gen(O,C)
x_OD = line_gen(O,D)
x_OY = line_gen(O,Y)


plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')
plt.plot(x_OX[0,:],x_OX[1,:],label='$OX$')

plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_OC[0,:],x_OC[1,:],label='$OC$')
plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$')
plt.plot(x_OY[0,:],x_OY[1,:],label='$OY$')

print("A",A)
print("B",B)

print("C",C)
print("D",D)
plt.text(0.1, 0.1 , 'O')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B')
plt.text(X[0] * (1 + 0.1), X[1] * (1 - 0.1) , 'X')

plt.text(C[0] * (1 + 0.1), C[1] * (1 - 0.1) , 'C')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')
plt.text(Y[0] * (1 + 0.1), Y[1] * (1 - 0.1) , 'Y')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/step2.pdf')
plt.savefig('./figs/step2.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/tri_icircle.pdf"))
#else
plt.show()
