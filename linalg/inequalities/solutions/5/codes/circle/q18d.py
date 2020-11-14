#Code by GVV Sharma
#December 9, 2019
#released under GNU GPL
#Circumcircle of a triangle
import numpy as np
import matplotlib.pyplot as plt
from coeffs18 import *

#if using termux
import subprocess
import shlex
#end if


len = 100

#Finding the circumcentre and radius
O = np.array([0.25,0])
R = 0.25
print("the center and the radius are ",O, R)

#Generating the circle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = R*np.cos(theta)
x_circ[1,:] = R*np.sin(theta)
x_circ = (x_circ.T + O).T




#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:])
plt.plot(O[0], O[1], 'o')
plt.text(O[0], O[1] , 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/q18d.pdf')
plt.savefig('./figs/q18d.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/tri_ccircle.pdf"))
#else
plt.show()

