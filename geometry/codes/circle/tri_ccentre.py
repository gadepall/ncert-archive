#Code by GVV Sharma
#December 7, 2019
#released under GNU GPL
#Drawing a triangle given 3 sides
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


#Triangle sides
a = 5
b = 6
c = 4

#Triangle vertices
A,B,C = tri_vert(a,b,c)

#Finding the circumcentre
p = np.zeros(2)
n1 = dir_vec(B,A)
p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
n2 = dir_vec(C,B)
p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
#Intersection
N=np.vstack((n1,n2))
O=np.linalg.inv(N)@p

print(A)
print(O)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')
plt.plot(x_OC[0,:],x_OC[1,:],label='$OC$')

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
plt.savefig('./figs/circle/tri_ccentre.pdf')
plt.savefig('./figs/circle/tri_ccentre.eps')
subprocess.run(shlex.split("termux-open ./figs/circle/tri_ccentre.pdf"))
#else
#plt.show()



