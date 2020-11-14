# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:44:47 2020

Course: EE5609 Matrix Theory (Assignment-2)

@author: kranthi Kumar P
"""

import numpy as np
#import matplotlib.pyplot as plt

# Function for shortest distance of a plane from point P
def DistancefromPlane(coeff,aug):
    # Input Arguments
    # coeff - Coefficients of linear equation
    # aug - augment of linear equation
    normal = coeff
    distance = np.abs(aug/np.linalg.norm(normal))
    return distance

# Problem (a)
A = np.array([0,0,1])
aug = 2
dist = DistancefromPlane(A,aug)
print("Shortest Distance of Plane from Origin is {0}".format(dist))

# Problem (b)
A = np.array([0,5,0])
aug = -8
dist = DistancefromPlane(A,aug)
print("Shortest Distance of Plane from Origin is {0}".format(dist))

# Problem (c)
A = np.array([1,1,1])
aug = 1
dist = DistancefromPlane(A,aug)
print("Shortest Distance of Plane from Origin is {0}".format(dist))

# Problem (d)
A = np.array([2,3,-1])
aug = 5
dist = DistancefromPlane(A,aug)
print("Shortest Distance of Plane from Origin is {0}".format(dist))
