#!/usr/bin/env python
# coding: utf-8

# In[10]:


#! /usr/bin/python3
import numpy as np

# Initialising the values of X and Y to verify problem (i)
X = np.array([[5,0],
             [1,4]])
Y = np.array([[2,0],
             [1,1]])

# Calculating the matrices X+Y,X-Y
XplusY = X + Y
XminusY = X - Y
print("X + Y =",XplusY)
print("X - Y =",XminusY)

# Initialising the values of X and Y to verify problem (ii)
X = np.array([[2/5,-12/5],
             [-11/5,3]])
Y = np.array([[2/5,13/5],
             [14/5,-2]])

# Calculating the matrices 2X+3Y,3X+2Y
X2plus3Y = 2*X + 3*Y
X3plus2Y = 3*X + 2*Y
print("2X + 3Y = ",X2plus3Y)
print("3X + 2Y = ",X3plus2Y)


# In[ ]:




