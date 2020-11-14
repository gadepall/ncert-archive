#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:55:48 2020

@author: pooja
"""

#%%
import numpy as np

#%%
def GramSchmidt(A):
    """
    The Gram-Schmidt method to A of size 2x2 and returns Q and R such that Q*R = A.
    """
    a1 = np.array([[3], [4]])
    a2 = np.array([[-2], [-2]])
    u1 = a1
    e1 = u1/np.linalg.norm(u1)
    u2 = a2 - (np.transpose(a2)@e1)*e1
    e2 = u2/np.linalg.norm(u2)
    Q = np.block([e1,e2])
    r11 = np.transpose(a1)@e1
    r12 = np.transpose(a2)@e1
    r22 = np.transpose(a2)@e2
    R = np.block([[r11, r12],[0, r22]])
    return Q, R

A = ([3, -2], [4, -2])
print ("The given matrix is \n")
print (A)
Q, R = GramSchmidt(A)
print ("The Q matrix is \n")
print (Q)
print ("The R matrix is\n")
print (R)
print ("Q^T*Q = ")
print (np.transpose(Q)@Q)
print ("Q*R =")
print (Q@R)
