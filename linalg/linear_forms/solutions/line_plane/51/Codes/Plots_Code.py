from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from coeffs import *

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


#Points on the lines AB and CD
A=np.array([-1,1]).reshape((2,1))
B=np.array([5,7]).reshape((2,1))
C=np.array([10,-6]).reshape((2,1))
D=np.array([1,3]).reshape((2,1))

#Generating the lines
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)

#Plotting the lines
plt.plot(x_AB[0,:],x_AB[1,:],label="AB")
plt.plot(x_CD[0,:],x_CD[1,:],label="[1 1]x=4")


#intersection point
P = np.array([[-1, 1], [1, 1]])
Q = np.array([[2], [4]])
X=np.linalg.inv(P) @ Q

#plotting point
ax.scatter(X[0],X[1],marker='o')
ax.text(1,3,0, "X(1,3,0)", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()
