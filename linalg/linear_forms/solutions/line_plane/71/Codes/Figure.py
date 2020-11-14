import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from mpl_toolkits.mplot3d import Axes3D

# Coordinates
x_s = [0,5]
y_s = [0,-2]
z_s = [0,3]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Adding Label
for x, y, z in zip(x_s, y_s, z_s):
    label = '(%d, %d, %d)' % (x, y, z)
    ax.text(x, y, z, label, zdir)

ax.scatter(x_s, y_s, z_s, c=['r','g'], marker='o')
plot, = ax.plot3D(x_s, y_s, z_s)

plt.show()
