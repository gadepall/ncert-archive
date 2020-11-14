# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:10:37 2020
Course: EE5609-Matrix Theory
@author: Kranthi Kumar
"""


# QR Decomposition of m x n matrix

import numpy as np

# Input Matrix
A=np.array([[3.,-1.],[-4.,2.]])
print("Given matrix A is: \n",A)

# Qr decomposition
Q,R=np.linalg.qr(A)
print("Orthogonal Matrix Q is :\n",Q)

print("Upper Triangular Matrix R is: \n",R)

#Verification Q^TQ=I
print("Q^TQ=\n",np.dot(Q.T,Q))
print("Verified Q^TQ = I\n")

print("QR=\n",np.dot(Q,R))
print("Hence proved A = QR")
