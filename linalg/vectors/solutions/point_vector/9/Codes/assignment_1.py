#! /usr/bin/python3
import numpy as np
k = 8
a = [2,2,3]
b = [-1,2,1]
c= [3,1,0]
d= [2-k , 2+2*k , 3+k]   #d=(a+kb)

ans = np.dot(c,d)

#dot product is zero if the two vectors are perpendicular
if ans == 0 :
  print("The vectors are perpendicular for value of k =", 8)
