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
O1 = np.array([2,4])
R1 = np.sqrt(65)
print("the center and the radius are ",O1, R1)

#Generating the circle
theta1 = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = R1*np.cos(theta1)
x_circ1[1,:] = R1*np.sin(theta1)
x_circ1 = (x_circ1.T + O1).T




#Plotting the circle
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$1st_circle$')
plt.plot(O1[0], O1[1], 'o')
plt.text(O1[0], O1[1] , 'O')


O2 = np.array([-4,5])
R2 = np.sqrt(53)
print("the center and the radius are ",O2, R2)

#Generating the circle
theta2 = np.linspace(0,2*np.pi,len)
x_circ2 = np.zeros((2,len))
x_circ2[0,:] = R2*np.cos(theta2)
x_circ2[1,:] = R2*np.sin(theta2)
x_circ2 = (x_circ2.T + O2).T




#Plotting the circle
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$2nd_circle$')
plt.plot(O2[0], O2[1], 'o')
plt.text(O2[0], O2[1] , 'O2')

O3 = np.array([5,-3])
R3 = 6
print("the center and the radius are ",O3, R3)

#Generating the circle
theta3 = np.linspace(0,2*np.pi,len)
x_circ3 = np.zeros((2,len))
x_circ3[0,:] = R3*np.cos(theta3)
x_circ3[1,:] = R3*np.sin(theta3)
x_circ3 = (x_circ3.T + O3).T




#Plotting the circle
plt.plot(x_circ3[0,:],x_circ3[1,:],label='$3rd_circle$')
plt.plot(O3[0], O3[1], 'o')
plt.text(O3[0], O3[1] , 'O3')




plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.legend(loc='upper right')
plt.axis('equal')

#if using termux
plt.savefig('./figs/circle/q18abc.pdf')
plt.savefig('./figs/circle/q18abc.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/tri_ccircle.pdf"))
#else
plt.show()

