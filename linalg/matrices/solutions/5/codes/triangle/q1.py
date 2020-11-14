from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from coeffs1 import *

#if using termux
import subprocess
import shlex
#end if

#Line points
A = np.array([1,1,1]) 
B = np.array([1,2,3]) 
C = np.array([2,3,1]) 

a = np.linalg.norm(B-C)
b = np.linalg.norm(C-A)
c = np.linalg.norm(A-B)

#Hero's formula
s = (a+b+c)/2
#print(s,a,b,c)
area = np.sqrt(s*(s-a)*(s-b)*(s-c))
print("Hero's formula", area)

area = 1/2*np.linalg.norm(np.cross(B-A,C-A))
print("Cross Product", area)


#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Vertices of 3D triangle
A = np.array([1,1,1]).reshape((3,1))
B = np.array([1,2,3]).reshape((3,1))
C = np.array([2,3,1]).reshape((3,1))

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)


#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="BC")
plt.plot(x_CA[0,:],x_CA[1,:],x_CA[2,:],label="CA")

#plotting point
ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.text(1,1,1, "A", color='red')
ax.text(1,2,3, "B", color='red')
ax.text(2,3,1, "C", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
plt.savefig('./figs/q1.pdf')
plt.savefig('./figs/q1.eps')
#subprocess.run(shlex.split("termux-open ./triangle/figs/triangle_3d.pdf"))
#else
plt.show()
