from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def dir_vec(A,B):
  return B-A

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

yy, zz = np.meshgrid(range(10), range(50))
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

xx = yy*0

A = np.array([4,8,10]).reshape((3,1))
B = np.array([6,10,-8]).reshape((3,1))
P = np.array([0,4,46]).reshape((3,1))

AB = line_gen(A,B)
AP = line_gen(A,P)

plt.plot(AB[0,:],AB[1,:],AB[2,:],label="AB")
plt.plot(AP[0,:],AP[1,:],AP[2,:],'--')

Plane=ax.plot_surface(xx,yy,zz,label="YZ-Plane",color='r',alpha=0.5)
Plane._facecolors2d=Plane._facecolors3d
Plane._edgecolors2d=Plane._edgecolors3d

ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(P[0],P[1],P[2],'o')
ax.text(4,8,13, "A", color='red')
ax.text(6,10,-5, "B", color='red')
ax.text(0,4,49, "P", color='red')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
