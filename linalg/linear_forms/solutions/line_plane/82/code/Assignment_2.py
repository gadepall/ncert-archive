import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline
import seaborn as sns
import math as m
# set normal vector, and point on plane
point=np.array([0,0,0])
normal = np.array([3, 5,6])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -7

# create x,y
xx, yy = np.meshgrid(range(10), range(10))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy -d) * 1. /normal[2]
z1=(-normal[0] * xx - normal[1] * yy +d) * 1. /normal[2]
# setup plot
plt3d = plt.figure(figsize=(10,10)).gca(projection='3d');
plt3d.set_xlabel('x');
plt3d.set_ylabel('y');
plt3d.set_zlabel('z');

# plot the surface
plt3d.plot_surface(xx, yy, z, alpha=0.7);
plt3d.plot_surface(xx, yy, z1, alpha=0.7);

# plot the point
plt3d.plot([point[0]], [point[1]], [point[2]], color='blue', marker='H', markersize=20, alpha=0.8);
plt3d.plot([point[0]], [point[1]], [point[2]], color='green', marker='H', markersize=20, alpha=0.8);

# set the normal vector to start at the center of the plane
startX = np.mean(plt3d.get_xlim())
startY = np.mean(plt3d.get_ylim())
startZ = (-normal[0] * startX - normal[1] * startY - d) * 1. /normal[2]
startZ1=(-normal[0] * startX - normal[1] * startY + d) * 1. /normal[2]


# plot the normal vector
plt3d.quiver([startX], [startY], [startZ], [normal[0]], [normal[1]], [normal[2]], linewidths = (5,), edgecolor="red")
plt3d.quiver([startX], [startY], [startZ1], [normal[0]], [normal[1]], [normal[2]], linewidths = (5,), edgecolor="green")
