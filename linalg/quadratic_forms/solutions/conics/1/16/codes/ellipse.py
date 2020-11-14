import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


O = np.array(([0,0])) # found from eq
f = 1  # solved from equation
a=3
b=4
q1=np.array(([0,4]))
q2=np.array(([0,-4]))
q3=np.array(([3,0]))
q4=np.array(([-3,0]))


# function to generate circle
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	x_ellipse = (x_ellipse.T + O).T
	return x_ellipse
   

##Generating the circle
x_ellipse= ellipse_gen(a,b)
plt.plot(x_ellipse[0,:],x_ellipse[1,:],label='$ellipse$')
plt.axhline(y=q1[1],color='r',label='$tangent1$')
plt.axhline(y=q2[1],color='r',label='$tangent2$')
plt.axvline(x=q3[0],color='g',label='$tangent3$')
plt.axvline(x=q4[0],color='g',label='$tangent4$')

#plotting and labelling of points
plt.plot(q1[0], q1[1], '.')
plt.text(q1[0] * (1 + 0.1), q1[1] * (1 + 0.1) , 'Q1(0,4)')
plt.plot(q2[0], q2[1], '.')
plt.text(q2[0] * (1 -0.06), q2[1] * (1+0.05) , 'Q2(0,-4)')
plt.plot(q3[0], q3[1], '.')
plt.text(q3[0] * (1 + 0.1), q3[1] * (1 - 0.1) , 'Q3(3,0)')
plt.plot(q4[0], q4[1], '.')
plt.text(q4[0] * (1 + 0.1), q4[1] * (1 - 0.1) , 'Q4(-3,0)')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()