#Code by GVV Sharma
#December 15, 2019
#released under GNU GPL
#Orthocentre of a triangle
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


#Triangle sides
a = 6
b = 5
c = 4

#Triangle vertices
A,B,C = tri_vert(a,b,c)
D =  alt_foot(A,B,C)
E =  alt_foot(B,C,A)
F =  alt_foot(C,A,B)

#Normal vectors of AD and BE
n1 = B-C
n2 = C-A

#Orthocentre
H =  line_intersect(n1,A,n2,B)

print(D,E,F,H)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(D,A)
x_BE = line_gen(B,E)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E')
plt.plot(H[0], H[1], 'o')
plt.text(H[0] * (1 + 0.03), H[1] * (1 - 0.1) , 'H')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/triangle/tri_alt_h.pdf')
plt.savefig('./figs/triangle/tri_alt_h.eps')
subprocess.run(shlex.split("termux-open ./figs/triangle/tri_alt_h.pdf"))
#else
#plt.show()







