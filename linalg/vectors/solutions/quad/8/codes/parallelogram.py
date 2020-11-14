from mpl_toolkits import mplot3d



#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

z_line1 = np.linspace(0, 4, 1000)
x_line1 = np.linspace(0, 3, 1000)
y_line1 = np.linspace(0, 1, 1000)
ax.plot3D(x_line1, y_line1, z_line1, 'blue',label='$OA$')
ax.plot(x_line1, y_line1, z_line1, 'blue',label='$OA$')

z_line2 = np.linspace(4, 5, 1000)
x_line2 = np.linspace(3, 4, 1000)
y_line2 = np.linspace(1, 0, 1000)
ax.plot3D(x_line2, y_line2, z_line2, 'orange',label='$AC$')

z_line3 = np.linspace(5, 1, 1000)
x_line3 = np.linspace(4, 1, 1000)
y_line3 = np.linspace(0, -1, 1000)
ax.plot3D(x_line3, y_line3, z_line3, 'red',label='$CB$')

z_line4 = np.linspace(1, 0, 1000)
x_line4 = np.linspace(1, 0, 1000)
y_line4 = np.linspace(-1, 0, 1000)
ax.plot3D(x_line4, y_line4, z_line4, 'green',label='$BO$')

z_point1 = 0
x_point1 = 0
y_point1 = 0
ax.scatter3D(x_point1, y_point1, z_point1, cmap='hsv');

z_point2 = 4
x_point2 = 3
y_point2 = 1
ax.scatter3D(x_point2, y_point2, z_point2, cmap='hsv');

z_point3 = 1
x_point3 = 1
y_point3 = -1
ax.scatter3D(x_point3, y_point3, z_point3, cmap='hsv');


z_point4 = 5
x_point4 = 4
y_point4 = 0
ax.scatter3D(x_point4, y_point4, z_point4,label='$C$', cmap='hsv');


ax.set_xlabel('$X$', fontsize=20, rotation=150)
ax.set_ylabel('$Y$',fontsize=20)
ax.set_zlabel(r'$Z$', fontsize=20)
#ax.yaxis._axinfo['label']['space_factor'] = 3.0
plt.show()
