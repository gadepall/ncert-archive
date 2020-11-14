import numpy as np
import matplotlib.pyplot as plt
import math

def curveFunction(x):
    return (x**2) - (2*x) + 7

def tangentLine(x):
    return (2*x) + 3


X_coord = np.array(np.linspace(-3,7,400))
Y_coord =curveFunction(X_coord)
y1 = np.zeros(len(X_coord))

for i in range(len(X_coord)):
    y1[i] = Y_coord[i]*-1


#plot points and lines
plt.plot(X_coord, Y_coord,'r', label='$y=x^2-2x+7$')
plt.plot(2, 7, 'o', label='Point of contact q=(2,7)')
X_coord = np.array(np.linspace(-3,7,400))
y2=tangentLine(X_coord)
plt.plot(X_coord,y2,  label='$y=2x+3$')
plt.text(2, 7,'$q$')



plt.axis('equal')
plt.legend(loc='best')
plt.grid()
plt.savefig('parallelLineTangent.png')
plt.show()