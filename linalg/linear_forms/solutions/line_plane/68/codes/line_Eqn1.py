from mpl_toolkits import mplot3d

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-5,5,100)
y = 2*x-5
z= -x + 6
#ax.plot3D(x, y, z, 'magenta',label='$a$')
ax.plot3D(x, y, z, 'magenta')

#plt.title('Graph of y=2x+1')

#z_line1 = 10* (np.linspace(0, -1, 1000))
#x_line1 = 10* (np.linspace(0, 1, 1000))
#y_line1 = 10* (np.linspace(0, 2, 1000))
#ax.plot3D(x_line1, y_line1, z_line1, 'red',label='$b$')

z_point1 = 4
x_point1 = 2
y_point1 = -1
ax.scatter3D(x_point1, y_point1, z_point1, cmap='hsv',label='$a$');


ax.set_xlabel('$X$', fontsize=10, rotation=150)
ax.set_ylabel('$Y$',fontsize=10)
ax.set_zlabel(r'$Z$', fontsize=10)

plt.legend(loc='upper left')
plt.grid()
plt.show()


