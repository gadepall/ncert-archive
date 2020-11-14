#Code by GVV Sharma
#November 25, 2019
#released under GNU GPL

#This program plots the circumcircle of Triangle ABC
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
import subprocess
import shlex
#end if

len = 100
p = np.zeros(2)

O = np.array([0, 0])
r = 3

#theta = np.linspace(0,2*np.pi,len)
#x_circ = np.zeros((2,len))
#x_circ[0,:] = r*np.cos(theta)
#x_circ[1,:] = r*np.sin(theta)
#x_circ = (x_circ.T + O).T

#Plotting all lines
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T



plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')


plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figures/circle/circle.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/circumcircle.pdf"))
#else
plt.show()


