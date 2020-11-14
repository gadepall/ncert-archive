from mpl_toolkits import mplot3d



#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

z_line1 = np.linspace(4, 2, 1000)
x_line1 = np.linspace(1, -4, 1000)
y_line1 = np.linspace(-3, 1, 1000)
ax.plot3D(x_line1, y_line1, z_line1, 'green',label='$OA$')
#ax.plot(x_line1, y_line1, z_line1, 'blue',label='$OA$')

z_point1 = 4
x_point1 = 1
y_point1 = -3
ax.scatter3D(x_point1, y_point1, z_point1, cmap='hsv');

z_point2 = 2
x_point2 = -4
y_point2 = 1
ax.scatter3D(x_point2, y_point2, z_point2, cmap='hsv');

ax.text(1,-3,4, "P", color='blue')
ax.text(-4,1,2, "Q", color='red')
#ax.text(3,-4,-4, "C", color='red')

#P = np.array([1,-3,4]).reshape((3,1))
#Q = np.array([-4,1,2]).reshape((3,1))

#x_PQ = line_gen(P,Q)
#plt.plot(x_PQ[0,:],x_PQ[1,:],x_PQ[2,:],label="AB")

ax.set_xlabel('$X$', fontsize=20, rotation=150)
ax.set_ylabel('$Y$',fontsize=20)
ax.set_zlabel(r'$Z$', fontsize=20)
#ax.yaxis._axinfo['label']['space_factor'] = 3.0
plt.show()
