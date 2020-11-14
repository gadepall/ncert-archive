#!/usr/bin/env python
# coding: utf-8

# In[18]:


#! /usr/bin/python3
import numpy as np

# Initialising a=2, b=3, c=4 and check if the determinant is equal to 1+a^2+b^2+c^2 = 30
X = np.array([[[5,6,8],
             [6,10,12],
             [8,12,17]]])

# Calculating the value of determinant
detValue = np.linalg.det(X)
print("Value of determinant = ", detValue)
print("Hence proved")

