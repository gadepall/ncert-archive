import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

def angle_lines(a,b):
    '''Function to find the angle between two lines given their direction vectors a and b'''
    ab_dot = np.dot(a,b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    cos_theta = ab_dot/(norm_a*norm_b)
    theta = np.arccos(cos_theta)
    theta = np.degrees(theta)
    return theta

#Solution verification cases, p = 70/11, putting this value in the direction vectors
a = np.array([-3,20/11,2])
b = np.array([-30/11,1,-5])
print("Angle between the two line in degrees is:")
print(angle_lines(a,b))


x1 = [-2,1]
y1 = [42/11,2]
z1 = [5,3]

x2 = [-19/11,1]
y2 = [6,5]
z2 = [1,6]



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot3D(x1, y1, z1,label = "L1",color='r',marker='o')
ax.plot3D(x2,y2,z2,label = "L2",color='b',marker='o')

for x, y, z in zip(x1, y1, z1):
    label = '(%d, %d, %d)' % (x, y, z)
    ax.text(x, y, z, label)

for x, y, z in zip(x2, y2, z2):
    label = '(%d, %d, %d)' % (x, y, z)
    ax.text(x, y, z, label)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.savefig("lines.png")
plt.show()