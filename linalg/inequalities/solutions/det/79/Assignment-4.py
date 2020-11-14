# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 09:10:12 2020
Course: EE5609 Matrix Theory
@author: kranthiKumar
"""
import numpy as np
import numpy.linalg as nlg

#Assign Variables
x = 2
y = 9
z = -4
p = 2.5

A = np.array([[x,x*x,(1+p*x*x*x)],
              [y,y*y,(1+p*y*y*y)],
              [z,z*z,(1+p*z*z*z)]
              ])

print(A)

#Left Hand Side
LHS = nlg.det(A)
print('LHS = {0}'.format(round(LHS,2)))

#Right Hand Side
RHS = (1+p*x*y*z)*(x-y)*(y-z)*(z-x)
print('RHS = {0}'.format(round(RHS,2)))

print("Hence Problem Statement Proved")
