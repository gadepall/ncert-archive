import matplotlib.pyplot as plt 
import numpy as np 
from coeffs import *
import subprocess
import shlex

A = np.array([0,2])
B = np.array([0,-2])
C = np.array([2*np.sqrt(3),0])
D = np.array([-2*np.sqrt(3),0])

x_AB = line_gen(A,B)
x_AC = line_gen(A,C)
x_BC = line_gen(B,C)
x_AD = line_gen(A,D)
x_BD = line_gen(B,D)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')

plt.plot(A[0], A[1], 'o')
plt.text(0, 2.2, 'A')

plt.plot(B[0], B[1], 'o')
plt.text(0, -2.2, 'B')

plt.plot(C[0], C[1], 'o')
plt.text(2*np.sqrt(3)+0.2,0, 'C')

plt.plot(D[0], D[1], 'o')
plt.text(-2*np.sqrt(3)-0.2,0, 'D')

plt.title('Equilateral triangle')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.show()
