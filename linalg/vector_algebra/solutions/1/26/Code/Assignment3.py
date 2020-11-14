from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Vertices of 3D triangle
A = np.array([0,0,0]).reshape((3,1))
B = np.array([4,-2,0]).reshape((3,1))
C = np.array([3,5,0]).reshape((3,1))
E = np.array([-3,5,0]).reshape((3,1))
D = np.array([3.5,1.5,0]).reshape((3,1))








#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CE = line_gen(C,E)
x_AE = line_gen(A,E)
x_AD = line_gen(A,D)
x_AC = line_gen(A,C)
x_DE = line_gen(D,E)

#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="BC")
plt.plot(x_CE[0,:],x_CE[1,:],x_CE[2,:],label="CE")
plt.plot(x_AE[0,:],x_AE[1,:],x_AE[2,:],label="AE")
plt.plot(x_AD[0,:],x_AD[1,:],x_AD[2,:],label="AD")
plt.plot(x_AC[0,:],x_AC[1,:],x_AC[2,:],label="AC")
plt.plot(x_DE[0,:],x_DE[1,:],x_DE[2,:],label="DE")

#plotting point
ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.scatter(E[0],E[1],E[2],'o')
ax.text(1,2,3, "A", color='red')
ax.text(-1,-2,-1, "B", color='red')
ax.text(2,3,2, "C", color='red')
ax.text(4,7,6, "E", color='red')







#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
#plt.savefig('./triangle/figs/quad_3d.pdf')
#plt.savefig('./triangle/figs/quad_3d.eps')
#subprocess.run(shlex.split("termux-open ./triangle/figs/quad_3d.pdf"))
#else
plt.show()
