import numpy as np
import matplotlib.pyplot as plt
import math



# equation - x^2 - 2*x
X_coord = np.array(np.linspace(2/3, 4.0, num=40))
Y_coord =[math.sqrt(3*num-2) for num in X_coord]
y1 = np.zeros(len(X_coord))

for i in range(len(X_coord)):
    y1[i] = Y_coord[i]*-1


#plot points and lines
plt.plot(X_coord, Y_coord,'r', label='$y^2=3x-2$')
plt.plot(X_coord, y1,'r')
plt.plot(41/48, -3/4, 'o', label='Point of contact q=(41/48,-3/4)')
X_coord = np.array(np.linspace(0.2, 4.0, num=40))
y2=(23/24)-(2*X_coord)
plt.plot(X_coord,y2,  label='$y+2x=23/24$')
plt.text(41/48, -3/4,'$q$')



plt.axis('equal')
plt.legend(loc='best')
plt.grid()
plt.show()
