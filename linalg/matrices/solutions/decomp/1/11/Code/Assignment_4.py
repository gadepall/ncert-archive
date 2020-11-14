import numpy as np 
import matplotlib.pyplot as plt 
import subprocess
import shlex

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


O = np.array([0,0])
B = np.array([-2,0])
A = np.array([0,2])
X = np.array([2,0])
Y = np.array([0,-2])

x_points_1 = [np.cos(theta*np.pi/180) for theta in range(46)]
y_points_1 = [np.sin(theta*np.pi/180) for theta in range(46)]

x_points_2 = [np.cos(theta*np.pi/180) for theta in range(46)]
y_points_2 = [0 for theta in range(46)]

x_points = x_points_1 + x_points_2
y_points = y_points_1 + y_points_2

x_AB = line_gen(A,B)
x_BX = line_gen(B,X)
x_AY = line_gen(A,Y)
len = 200
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = np.sqrt(4)*np.cos(theta)
x_circ[1,:] = np.sqrt(4)*np.sin(theta)
x_circ = (x_circ.T + O).T

plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')


plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BX[0,:],x_BX[1,:])
plt.plot(x_AY[0,:],x_AY[1,:])

plt.text(B[0],B[1]+ 0.1,'B')
plt.text(A[0],A[1]+0.1,'A')
plt.text(O[0],O[1]+0.1,'O')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.savefig('circle.png')
plt.show()
