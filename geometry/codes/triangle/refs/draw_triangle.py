#Code by GVV Sharma
#March 26, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


#Triangle sides
#a = 4
#b = 5
#c = 6
#p = (a**2 + c**2-b**2 )/(2*a)
#q = np.sqrt(c**2-p**2)

#Triangle vertices
A = np.array([1,3]) 
B = np.array([-2,-2]) 
C = np.array([4,-1]) 

#Incentre
k1 = 1
k2 = 1
I,r = icentre(A,B,C,k1,k2)
print(I,r)
#Incentre
k1 = 1
k2 = 1
O,R = ccircle(A,B,C)
#print(O,R)

D = alt_foot(I,B,C)
E = alt_foot(I,C,A)
F = alt_foot(I,A,B)
#
print(D,E,F)
n1 = omat@(O-A)
n2 = omat@(B-C)
P = line_intersect(n1,A,n2,B)
N=np.vstack((n1,n2))

#print (n1,n2,N)
#print(P)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
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
plt.savefig('./figs/triangle_ang_bisec_py.pdf')
plt.savefig('./figs/triangle_ang_bisec_py.eps')
subprocess.run(shlex.split("termux-open ./figs/triangle_ang_bisec_py.pdf"))
#else
#plt.show()







