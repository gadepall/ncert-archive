# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:52:19 2020

@author: Satyanarayana
"""

import numpy as np

#Let A ,B,C and D represent the vertices of the parallelogram
A = np.array([0,0])
B = np.array([2,4])
C= np.array([6,0])
D = np.array([4,0])

#side1 and side2 represent the sides of the parallelogram
Side1 = D - A
Side2 = B - A

Diagonal1 = Side1+Side2
Diagonal2= Side1-Side2


#Sum of the squares of the diagonal 
Diagonal_square_sum = Diagonal1.dot(Diagonal1)+Diagonal2.dot(Diagonal2)


#Sum of the squares of the sides 
Side_square_sum = 2*(Side1.dot(Side1)+Side2.dot(Side2))

print("The sum of squares of diagonals ={} is equal to \
      \n sum of squares of sides={} in a parallelogram\
      ".format(Diagonal_square_sum,Side_square_sum))
