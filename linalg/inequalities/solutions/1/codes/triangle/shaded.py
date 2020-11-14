#Code by GVV Sharma
#December 25, 2019
#Released under GNU GPL
#Solving linear inequalities

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


#Line Parameters
n1 = np.array([1,-1])
n2 = np.array([3,2])
n3 = np.array([0,1])
c =  np.array([-1,12])

c1 = -1
c2 = 12
c3 = 0
#Intercept 1
e1 = np.array([1,0]) 
e2 = np.array([0,1]) 
A1= c1*e1/(n1@e1)
B1 = c1*e2/(n1@e2)
k1 = 0
k2 = 3
N=np.vstack((n1,n2))
D1=np.linalg.inv(N)@c
x_A1B1 =  line_dir_pt(n1,D1,k1,k2)
plt.plot(x_A1B1[0,:],x_A1B1[1,:],label='$line1$')

#Intercept2
A2 = c2*e1/(n2@e1)
B2 = c2*e2/(n2@e2)
x_A2B2 =   line_gen(A2,B2)
plt.plot(x_A2B2[0,:],x_A2B2[1,:],label='$line2$')


#Intersection of the lines
A=line_intersect(n1,c1,n2,c2)
B=line_intersect(n2,c2,n3,c3)
C=line_intersect(n3,c3,n1,c1)

points = np.array((A,B,C))

#Filling up the desired region
plt.fill(points[:,0], points[:,1], alpha=0.5)

#Plotting points of Intersection
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 ) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 ), B[1] * (1)+0.1 , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 - 0.05), C[1] * (1 - 0.1) , 'C')
plt.plot(B2[0], B2[1], 'o')
plt.text(B2[0] * (1 ), B2[1] * (1)+0.1 , 'B2')
plt.plot(B1[0], B1[1], 'o')
plt.text(B1[0] * (1 ), B1[1] * (1)+0.1 , 'B1')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

plt.show()







