# -*- coding: Question 2.25 -*-
"""collinear.ipynb
Automatically generated by Colaboratory.
Original file is located at
       https://colab.research.google.com/drive/1cnQXwbBhhGTMapGFGBphdlmno5uR-bbY
"""

#Code by B.Valli Devi
#July 24, 2021




import matplotlib.pyplot as plt 
import numpy as np 

import subprocess
import shlex

plt.axis([-6,12,-6,12])

plt.axis('on')

A = np.array([6,5])
C = np.array([0,9])
B = np.array([-4,3])

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x_AC = line_gen(A,C)
x_BC = line_gen(B,C)



plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')


plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')

plt.text (6,5,'A(6,5)')
plt.text(-4,3,'B(-4,3)')
plt.text(0,9,'C(0,9)')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.show()
