import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#finding solution of two linear equation, this will give the foot of the perpendicular
A = np.array([[4,7],[2,-3]])
B = np.array([3,-1])
print(np.linalg.inv(A).dot(B))  #this line gives the point of intersection 

#Plotting for showing the graph :

#Inputs
M = np.array([0,3/7]) #a point satisfying equation of given line
N = np.array([3/4,0])  # another point satisfying equation of given line
O = np.array([1,1])  # point for second line
P = np.array([2/26,5/13]) #point of intersection found by solving the pblm
Q =np.array([6/13,0])#point on the new line 
R =np.array([0,6/13])#point on the new line 

#Generating all lines
x_AB = line_gen(M,N)
x_CD = line_gen(O,P)
x_EF =line_gen(Q,R)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')

plt.plot(M[0], M[1], 'o')
plt.plot(N[0], N[1], 'o')
plt.plot(O[0], O[1], 'o')
plt.plot(P[0], P[1], 'o')
plt.plot(Q[0], Q[1], 'o')
plt.plot(R[0], R[1], 'o')


plt.annotate("Desired Point (1/13,5/13 )", (P[0], P[1]))
plt.annotate("x intercept (6/13,0 )", (Q[0], Q[1]))
plt.annotate("y intercept (0,6/13 )", (R[0], R[1]))

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
