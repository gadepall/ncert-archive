import numpy as np
import matplotlib.pyplot as plt
import math
from line.funcs import *

#if using termux
import subprocess
import shlex
#end if
angQ,angR,r=[int(x) for x in input("Enter the angle Q ,angle R and PQ distance  : example 105 40 5 :").split()]

#To find angle P
angP = 180 - (angQ + angR) 

#To find q
q = (math.sin(math.radians(angQ))/math.sin(math.radians(angR)))*r

#To find coordinate of R(x,y)
x = (math.cos(math.radians(angP)))*q
y = (math.sin(math.radians(angP)))*q

#Triangle vertices
P = np.array([0,0])
Q= np.array([r,0])
R = np.array([x,y])


#Generating lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_PR = line_gen(P,R)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.02), Q[1] * (1) , 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.003), R[1] * (1 - 0.1) , 'R')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()
