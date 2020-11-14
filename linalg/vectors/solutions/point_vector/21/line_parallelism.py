# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:28:29 2020

@author: Pooja H; 
AI20MTECH14003
"""

# This program is to check whether two vectors are parallel or not.

#%%
# import the required library files
import numpy as np

#%%
class point_3d:
    # Vector initialization
    def __init__(self, x_data, y_data, z_data):
        self.x = x_data
        self.y = y_data
        self.z = z_data
      
# Fundction to verify vector parallelism
def verify(p1, p2, p3, p4):
    #Direction vector for the first line
    v1 = [p2.x - p1.x, p2.y - p1.y, p2.z - p1.z]
    
    #Direction vector for the second line
    v2 = [p4.x - p3.x, p4.y - p3.y, p4.z - p3.z]

    if(sum(np.cross(v1,v2))==0):
        print("The lines are parallel")
    else:
        print(" Not parallel")
#%%
#line 1             
point1 = point_3d(4, 7, 8)
point2 = point_3d(2, 3, 4)

#line 2
point3 = point_3d(-1, -2, 1)
point4 = point_3d(1, 2, 5)

#To verify whether the lines are parallel or not
verify(point1, point2, point3, point4)
