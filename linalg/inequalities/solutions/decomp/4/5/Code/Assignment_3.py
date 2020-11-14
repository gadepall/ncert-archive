from coeffs import *
from cvxpy import *
import numpy as np
import matplotlib.pyplot as plt
#from numpy import matrix

#if using termux
import subprocess
import shlex
#end if

A = np.array(( [3, 5], [5, 2 ])).T
b = np.array([ 15, 10 ]).reshape((2,-1))
c = np.array([ 5, 3 ])

x = Variable((2,1),nonneg=True)
#Cost function
f = c@x
obj = Maximize(f)
#Constraints
constraints = [A.T@x <= b]

#solution
Problem(obj, constraints).solve()

print(f.value,x.value)

#Line Parameters
n1 = np.array([3,5])
n2 = np.array([5,2])
#n3 = np.array([2,-3])

c1 = 15
c2 = 10
#c3 = 6

#Plotting Line 1
e1 = np.array([1,0])
e2 = np.array([0,1])
A = c1*e1/(n1@e1)
B = c1*e2/(n1@e2)
#Generating Line 1
O = np.array([0,0])
X = np.array([6,0])
Y = np.array([0,6])
x_AB = line_gen(A,B)
x_OX = line_gen(O,X)
x_OY = line_gen(O,Y)

#Plotting Line 1
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(x_OX[0,:],x_OX[1,:])
plt.plot(x_OY[0,:],x_OY[1,:])

plt.text(X[0],X[1]+ 0.1,'X')
plt.text(Y[0],Y[1]+0.1,'Y')
#Plotting Line 2
C = c2*e1/(n2@e1)
D = c2*e2/(n2@e2)
#Generating Line 1
x_CD = line_gen(C,D)

#Plotting Line 1
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.1), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.2), D[1] * (1) , 'D')

#Intersection of the lines
P = line_intersect(n1,c1,n2,c2)

#Plotting points of Intersection
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 ) , 'P')
plt.text(O[0],O[1]+0.1,'O')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
