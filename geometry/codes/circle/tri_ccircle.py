#Code by GVV Sharma
#December 9, 2019
#released under GNU GPL
#Circumcircle of a triangle
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


len = 100

#Triangle sides
a = 5
b = 6
c = 4

#Triangle vertices
A,B,C = tri_vert(a,b,c)

#Finding the circumcentre and radius
O = tri_ccentre(A,B,C)
R = tri_cradius(a,b,c)

#Mid points of the sides
D = (B+C)/2
E = (C+A)/2
F = (A+B)/2

print(A)
print(O, R)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)
x_OD = line_gen(O,D)
x_OE = line_gen(O,E)
x_OF = line_gen(O,F)

#Generating the circle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = R*np.cos(theta)
x_circ[1,:] = R*np.sin(theta)
x_circ = (x_circ.T + O).T

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')
plt.plot(x_OC[0,:],x_OC[1,:],label='$OC$')
plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$')
plt.plot(x_OE[0,:],x_OE[1,:],label='$OE$')
plt.plot(x_OF[0,:],x_OF[1,:],label='$OF$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/circle/tri_ccircle.pdf')
plt.savefig('./figs/circle/tri_ccircle.eps')
subprocess.run(shlex.split("termux-open ./figs/circle/tri_ccircle.pdf"))
#else
#plt.show()



