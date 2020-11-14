import numpy as np
import matplotlib.pyplot as plt
import math
#from coeffs import *
import subprocess
import shlex

#sides of triangle
a = 3
b = 5
c = 6

#coordinates of A
x=(a**2 + c**2 -b**2)/(2*a)
y=np.sqrt(c**2-x**2)

#generating the line points
def line_gen(A,B):
	len = 20
	dim = A.shape[0]
	x_AB = np.zeros((dim,len))
	lam_1 = np.linspace(0,1,len)
	for i in range(len):
		temp1 = A + lam_1[i]*(B-A)
		x_AB[:,i]=temp1.T
	return x_AB

#vertices
A = np.array([0,0])
P= np.array([3,0])
Q = np.array([1.5, 2.598])
AB = P + Q
B = np.array([3,1.732])
#C= np.array([(a/2)+5,0])
#D = np.array([(a/2)+5,0])



#Generating the lines
x_AP = line_gen(A,P)
x_AQ = line_gen(A,Q)
x_AB = line_gen(A,B)
x_PB = line_gen(P,B)
x_QB = line_gen(Q,B)

#plotting the all lines
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_AQ[0,:],x_AQ[1,:],label='$AQ$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_PB[0,:],x_PB[1,:],label='$PB$')
plt.plot(x_QB[0,:],x_QB[1,:],label='$QB$')


plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1), P[1]*(1-0.1), 'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1), Q[1]*(1), 'Q')
plt.plot(A[0], A[1], 'o')
plt.text(A[0]*(1+0.03), A[1]*(1-0.1),'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0]*(1+0.03), B[1]*(1-0.1),'B')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('angle.eps')

plt.show()
