#Code by GVV Sharma
#December 6, 2019
#released under GNU GPL
#Drawing a right angled triangle

import numpy as np
import matplotlib.pyplot as plt
from coeffs12 import *

#if using termux
import subprocess
import shlex
#end if

#Sides
a = 35
c = 12
#Triangle vertices
A = np.array([-c,a]) 
B = np.array([0,0]) 
C = np.array([-c,0]) 


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],':',label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('./figs/q12.pdf')
plt.savefig('./figs/q12.eps')
##subprocess.run(shlex.split("termux-open ./figs/triangle/tri_polar.pdf"))
#else
plt.show()
#A(-12,35)
#B(0,0)
#C(-12,0)
#AB = (12,-35)
#AC= (0,-35)
#AB.T AC =35*35
#COS(THETA)*AB*AC
#COS(THETA)*37*25
#COS(THETA) = 0.9459
