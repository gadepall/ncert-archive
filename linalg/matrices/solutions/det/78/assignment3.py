#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:12:22 2020

@author: shantanu
"""

import numpy as np

a,b,c=input("Enter the three parameter values : alpha beta gamma \n").split(" ")
a=int(a)
b=int(b)
c=int(c)

A=np.array([[a,a**2,b+c],[b,b**2,c+a],[c,c**2,a+b]])
print(A)
detA = np.linalg.det(A)
print("The determinant of the matrix A is :");print(round(detA))

val_exp=(b-c)*(c-a)*(a-b)*(a+b+c)
print("The value of (b-c)(c-a)(a-b)(a+b+c) = ");print(val_exp)


      

