#!/usr/bin/env python
# coding: utf-8

# In[7]:


## ! /usr/bin/python3
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#Initialising arays for storing 5 coordinates
X_axis = [0]*5
Y_axis = [0]*5
Z_axis = [0]*5

#Calculating 5 points which lie on the line from the parametric form 
for t in range(-2,3):
    X_axis[t] = 3*t + 5
    Y_axis[t] = 7*t - 4
    Z_axis[t] = 2*t + 6
    
#Adding point(5,4,-6) to show that the line passes through this point for t=0 
X_point = 5
Y_point = -4
Z_point = 6
    
#A 3D empty axis to plot the points
graph_basic = plt.axes(projection='3d')

#Plot the line in the 3D system using the defined points
graph_basic.plot3D(X_axis,Y_axis,Z_axis,label='Fig:A straight line in 3D space')

#Point the (5,-4,6) on the line
graph_basic.scatter3D(X_point, Y_point, Z_point, c='red')




