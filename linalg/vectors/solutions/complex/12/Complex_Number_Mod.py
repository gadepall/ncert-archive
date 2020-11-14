# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:15:47 2020

@author: Pooja H
ID: AI20MTECH14003

This program is used to compute the modulues of complex numbers
"""
#%%

import numpy as np
import cmath

#%%
# Read the complex numbers
x = 2
y = -1
z1 = complex(x, y)
p = 1
q = 1
z2 = complex(p, q)
print("The complex numbers are:")
print (z1, z2)
#Compute z1 + z1 + 1 and z1 - z2 + 1
sum_1 = z1 + z1 + complex(1)
sum_2 = z1- z2 + complex(1)

#Compute the modulus of a complex number
res_1 = sum_1/sum_2
modulus = np.linalg.norm(res_1)
print("\nThe result due to modulus operation")
print(modulus)