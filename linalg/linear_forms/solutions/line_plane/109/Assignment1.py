# -*- coding: utf-8 -*-
"""
@author: Satyanarayana
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

def plot_lines(x,y,z,k,l):

   ax.plot3D(x, y, z, k,label=l)

# l1_dir and l2_dir   
l1_dir = np.array([3, -16, 7])
l2_dir = np.array([3, 8, -5])
perpendicular_dir = np.array([2, 4, 6])

#points through which the lines pass
point1 = np.array([8,-19,10])
point2 = np.array([15,29,5])
point3 = np.array([1,2,-4])

#x1,y1,z1 are points on l1   
#x2,y2,z2 are points on l2 
#x3,y3,z3 are points on lper
x1 = [];y1 = [];z1 = []
x2 = [];y2 = [];z2 = []
x3 = [];y3 = [];z3 = []

#Compute points on 3 lines for plotting
for i in range(-10,20):
    
    x1 +=[l1_dir[0]*i+point1[0]];y1 +=[l1_dir[1]*i+point1[1]]; z1 +=[l1_dir[2]*i+point1[2]]
    x2 +=[l2_dir[0]*i+point2[0]];y2 +=[l2_dir[1]*i+point2[1]];z2 +=[l2_dir[2]*i+point2[2]]
    x3 +=[perpendicular_dir[0]*i+point3[0]]; y3 +=[perpendicular_dir[1]*i+point3[1]]; z3 +=[perpendicular_dir[2]*i-point3[2]]
    
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plot_lines(x1,y1,z1,'gray','line1')
plot_lines(x2,y2,z2,'green','line2')
plot_lines(x3,y3,z3,'red','perpendicular')
ax.legend()
ax.scatter(point3[0],point3[1],point3[2])    
plt.show()