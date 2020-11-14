import numpy as np
import matplotlib.pyplot as plt
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




A = np.array([1,-5])
B = np.array([-4,5])
C = np.array([-1.5,0])





#Generating the lines
x_AB = line_gen(A,B)





#plotting the all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')



plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1), A[1]*(1-0.1), 'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.2), B[1]*(1), 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1+0.03), C[1]*(1-0.1),'C')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('../figures/line/point_on_line/point_on_line.eps')

plt.show()
