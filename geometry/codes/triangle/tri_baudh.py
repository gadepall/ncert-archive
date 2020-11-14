#Code by GVV Sharma
#December 7, 2019
#released under GNU GPL
#Proof of Baudhyana Theorem

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#Sides
a = 4
c = 3
b = np.sqrt(a**2+c**2)

#Trigonometric ratios
st = c/b
ct = a/b

#perp distance
r = a*st



#Triangle vertices
A = np.array([0,c]) 
B = np.array([0,0]) 
C = np.array([a,0]) 

#Foot of perpendicular
p = r*st
q = r*ct
D = np.array([p,q]) 


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_BD = line_gen(B,D)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/triangle/tri_baudh.pdf')
plt.savefig('./figs/triangle/tri_baudh.eps')
subprocess.run(shlex.split("termux-open ./figs/triangle/tri_baudh.pdf"))
#else
#plt.show()







