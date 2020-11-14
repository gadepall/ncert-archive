import numpy as np
import matplotlib.pyplot as plt
#from coeffs import *

import subprocess
import shlex

#Inputs
#l1
#n1 = [1, -7]
#c1 = -5
#Plotting all lines
x = np.linspace(-10, 10, 200)
y1 = (x + 5)/7
y2 = 21 - 7*x
#fig = plt.figure()
#ax = fig.add_subplot(111)
plt.plot(x,y1, label = '-x + 7y = -5')
plt.plot(x,y2, label = '7x + y = 21')
plt.plot(3, 0, 'ro', label = 'x intercept = (3, 0)')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend()
#plt.axis('square')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.savefig('a1.png')
#plt.show()

