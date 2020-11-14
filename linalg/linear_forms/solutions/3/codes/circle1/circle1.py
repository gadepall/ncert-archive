#Code by GVV Sharma
#December 7, 2019
#released under GNU GPL
#Drawing a triangle given 3 sides
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

A=np.array([2,-2])
B=np.array([3,4])
#Finding the centre
p = np.zeros(2)
n1 = A-B
p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
n2 =np.array([1,1])
p[1] = 2
#Intersection
N=np.vstack((n1,n2))
O=np.linalg.inv(N)@p

print(O)
r1=np.linalg.norm(O-A)
r2=np.linalg.norm(O-B)
print(r1)
print(r2)
r=r1
#Generating all lines
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)

#Plotting all lines
plt.plot(x_OA[0,:],x_OA[1,:],label='$radius$')
#plt.plot(x_OB[0,:],x_OB[1,:])
#plotting circle
len=100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')


#plotting points
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')
plt.savefig('./pyfigs/circle1.eps')
plt.show()

