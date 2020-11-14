#Code by GVV Sharma
#December 10, 2019
#released under GNU GPL
#Incentre of a triangle
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

#Intriangle vertices
D,E,F = intri_vert(a,b,c)

#Finding the incircle
I = tri_ccentre(D,E,F)

#Finding the inradius
r = tri_iradius(a,b,c)

print(A)
print(I,r)
print(D,E,F)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_ID = line_gen(I,D)
x_IE = line_gen(I,E)
x_IF = line_gen(I,F)

#Generating the circle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + I).T

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_ID[0,:],x_ID[1,:],label='$ID$')
plt.plot(x_IE[0,:],x_IE[1,:],label='$IE$')
plt.plot(x_IF[0,:],x_IF[1,:],label='$IF$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$incircle$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 + 0.1), I[1] * (1 - 0.1) , 'I')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/circle/tri_icircle.pdf')
plt.savefig('./figs/circle/tri_icircle.eps')
subprocess.run(shlex.split("termux-open ./figs/circle/tri_icircle.pdf"))
#else
#plt.show()



