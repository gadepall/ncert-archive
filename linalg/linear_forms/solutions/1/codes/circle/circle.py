#Code by GVV Sharma
#March 6, 2019
#released under GNU GPL

#This program plots the incircle of Triangle ABC
import numpy as np
import matplotlib.pyplot as plt


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

len = 100

I=np.array([2,-3])
r=7.07
B=np.array([1,4])
A=2*I-B
print(A)
#Generating circle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + I).T

x_AB = line_gen(A,B)
#Plotting circle
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$incircle$')

plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 + 0.1), I[1] * (1 - 0.1) , 'O')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()


