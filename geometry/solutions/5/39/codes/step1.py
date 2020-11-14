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
#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.plot(r*np.cos(3.14/4),r*np.sin(3.14/4),'o')
plt.plot(r*np.cos(-3.14/4),r*np.sin(-3.14/4),'o')
plt.plot(1.414,0,'o')
plt.plot(0, 0, 'o')

x_AB = line_gen(A,B)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OX = line_gen(O,X)
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')
plt.plot(x_OX[0,:],x_OX[1,:],label='$OX$')

print("B",B)
print("A",A)
plt.text(0.1, 0.1 , 'O')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B')
plt.text(X[0] * (1 + 0.1), X[1] * (1 - 0.1) , 'X')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/step1.pdf')
plt.savefig('./figs/step1.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/tri_icircle.pdf"))
#else
plt.show()
