#Code by GVV Sharma
#December 9, 2019
#released under GNU GPL
#Circumcircle of a triangle
import numpy as np
import matplotlib.pyplot as plt
#from coeffs import *

#if using termux
import subprocess
import shlex
#end if


len = 100

#Finding the circumcentre and radius
O = np.array([0,0])
R = 1
print("the center and the radius are ",O, R)

#Generating the circle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = R*np.cos(theta)
x_circ[1,:] = R*np.sin(theta)
x_circ = (x_circ.T + O).T

#shading part
theta1 = np.linspace(0,0.45*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = R*np.cos(theta1)
x_circ1[1,:] = R*np.sin(theta1)
x_circ1 = (x_circ1.T + O).T


t = np.arange(0,1.1)
plt.plot(t,t,'*-r')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:])
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), 0.1 , 'O')
plt.plot(0.707, 0.707, 'o')
plt.text(0.707,0.8, 'A')
plt.plot(1,0, 'o')
plt.text(1.1,0 , 'C')
plt.plot(0.707,0, 'o')
plt.text(0.707,-0.1 , 'B')

#plt.plot(x_circ1[0,:],x_circ1[1,:])
#plt.fill_between(x_circ1[0,:],x_circ1[1,:], color = "red", alpha = 0.4, hatch = '+')
#plt.fill_between(t,t)


plt.fill_between(t,t, color = "red",alpha=0.9)
#, color = "none",alpha = 0.3, hatch = '|')
#plt.fill_between(x_circ[0,:],x_circ[1,:], color = "yellow", alpha = 0.2, hatch = '+')


plt.fill_between(x_circ[0,:],x_circ[1,:], color = "yellow", alpha = 0.4, hatch = '+')

#,where=(x_circ[0,:]>0,x_circ[1,:]>0))
# The point of intersection of the line and the circle is (0.707,0.707) . hence the integrals have limits 0-->0.707 ;;; 0.707-->1

plt.fill_between(t,0)
A = np.array([0.707,0.707])
C = np.array([1,0])
B = np.array([0.707,0])
qw = np.linalg.norm(B-A)

er =np.linalg.norm(O-A)
ty = np.linalg.norm(B-O)
cang = (-qw**2+er**2+ty**2)/(2*er*ty)
print("angle = ",cang)
import math
OAB = math.acos(cang)
print(OAB)
areareq = (OAB*180/3.14)/360 * 3.14 * 1*1



#from sympy import *
#x, y = symbols('x y') 
#gfg_exp = x  
#gfg_expt = sqrt((1-x**2))

# Use sympy.integrate() method 
#a =integrate(gfg_exp, (x, 0, 0.707))
#b=integrate(gfg_expt, (x, 0.707,1) )
#print("B====",b+a)
#b+a
print("REQUIRED AREA = ",areareq)
      #3.14/4 - 0.3926)



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/q17.pdf')
plt.savefig('./figs/q17.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/tri_ccircle.pdf"))
#else
plt.show()


