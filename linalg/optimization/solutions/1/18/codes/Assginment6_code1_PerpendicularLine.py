import numpy as np
import matplotlib.pyplot as plt
import math

def curveFunction(x):
    return (x**2) - (2*x) + 7

def tangentLine(x):
    return (1/15)*((3405/36) - (5*x))


X_coord = np.array(np.linspace(-3,7,400))
Y_coord =curveFunction(X_coord)


#plot points and lines
plt.plot(X_coord, Y_coord,'r', label='$y=x^2-2x+7$')
plt.plot(5/6, 217/36, 'o', label='Point of contact q=(5/6,217/36)')
X_coord = np.array(np.linspace(-3,7,400))
y2=tangentLine(X_coord)
plt.plot(X_coord,y2,  label='$5x+15y=(3405/36)$')
plt.text(5/6, 217/36,'$q$')



plt.axis('equal')
plt.legend(loc='best')
plt.grid()
plt.savefig('perpendicularLineTangent.png')
plt.show()