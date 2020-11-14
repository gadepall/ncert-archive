import numpy as np
import matplotlib.pyplot as plt
import math

def curveFunction(x):
    return (x**2) - (2*x) + 7

def tangentLineParallel(x):
    return (2*x) + 3

def tangentLinePerpendicular(x):
    return (1/15)*((3405/36) - (5*x))


X_coord = np.array(np.linspace(-3,7,400))
Y_coord =curveFunction(X_coord)


plt.figure(num=None, figsize=(8, 6), dpi=80)

#plot points and lines
plt.plot(X_coord, Y_coord,'r', label='$y=x^2-2x+7$')
plt.plot(2, 7, 'o', label='Point of contact q1=(2,7)')
X_coord = np.array(np.linspace(-3,7,400))
y2=tangentLineParallel(X_coord)
plt.plot(X_coord,y2,  label='$y=2x+3$')
plt.text(2, 7,'$q1$')

plt.plot(5/6, 217/36, 'o', label='Point of contact q2=(0.83334,6.027778)')
X_coord = np.array(np.linspace(-3,7,400))
y2=tangentLinePerpendicular(X_coord)
plt.plot(X_coord,y2,  label='$5x+15y=94.58334$')
plt.text(5/6, 217/36,'$q2$')


plt.axis([-10, 10, -10, 20])
# plt.axis('equal')
plt.legend(loc='best')
plt.grid()
plt.savefig('parallelPerpendicularLineTangent.png')
plt.show()