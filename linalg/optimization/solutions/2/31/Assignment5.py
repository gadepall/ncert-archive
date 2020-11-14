# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 03:47:40 2020

@author: Rubeena
"""

import numpy as np
Q=np.array([[0.4472,0.8944],[0.8944,-0.4472]])
R=np.array([[2.236,4.919],[0,0.8944]])
result=Q@R
print(result)