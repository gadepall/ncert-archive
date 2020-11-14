#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:32:40 2020

@author: shantanu
"""

import numpy as np
import math as m

A=np.array(([3,-4],[-4,-3]))
Q=np.array(([3/m.sqrt(5),-4/m.sqrt(5)],[-4/m.sqrt(5),-3/m.sqrt(5)]))
R=np.array(([m.sqrt(5),0],[0,m.sqrt(5)]))

Abar=Q@R
print("The matrix A is : \n",A)
print("The matrix QR is \n:",Abar)
