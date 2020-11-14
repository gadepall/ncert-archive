# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np

# Equation to solve => (a.T)(b x c) + (b.T)(a x c) + (c.T)(a x b)

# declaring vectors
a = np.array([ [1] , [0] ,[0]])
b = np.array([ [0] , [1] ,[0]])
c = np.array([ [0] , [0] ,[1]])

# solution to equation
sol = np.dot(a.T,(np.cross(b,c, axis=0))) + np.dot(b.T,(np.cross(a,c, axis=0))) + np.dot(c.T,(np.cross(a,b, axis=0)))
print ("Solution to problem is : ", sol)