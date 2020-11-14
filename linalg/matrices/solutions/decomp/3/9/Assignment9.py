#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 00:58:29 2020

@author: Pooja
AI20MTECH14003
"""
#%%
import numpy as np

#%%
# Compute M = USV'

M = np.array([[-3, -30/7], [-20/7, 1], [2, -5]])
b = np.array([[2],[-1],[3]])
U, S, V = np.linalg.svd(M)
V = -V
mp_s = np.zeros(M.shape)
mp_s[0, 0] = 1/S[0]
mp_s[1, 1] = 1/S[1]
mps = np.transpose(mp_s)

x1 = V@mps@np.transpose(U)@b
mtm = np.transpose(M)@M
x2 = (np.linalg.inv(mtm))@(np.transpose(M)@b)
print("Using SVD, x is:\n")
print(x1)
print("Substituing the values for M and b to the standard equation, x is:\n")
print(x2)
