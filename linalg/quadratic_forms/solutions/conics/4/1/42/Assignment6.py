# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:39:23 2020

@author: Sandhya Addetla , AI20RESCH14001
"""
import numpy as np
A= np.array([[19,12],[12,1]])
print("Given matrix: ")
print(A)
a = A[:,0]
b = A[:,1]
#print(a, b)


u1 = np.linalg.norm(a)
q1 = a /u1
#print (u1, q1)

u3 = np.dot(q1,b)
#print (u3)

q2 = (b - u3*q1)/np.linalg.norm(b - u3*q1)
#print(q2)

u2 = np.dot(q2,b)
#print(u2)

Q = np.zeros(A.shape)
Q[:, 0] = q1
Q[:, 1] = q2

R = np.array([[u1, u3],[0, u2]])
print("Q =  {}".format(Q))
print("R = {} ".format(R))

A = Q@R
print("product of Q & R is")
print(A)
