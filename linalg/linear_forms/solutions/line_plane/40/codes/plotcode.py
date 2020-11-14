import numpy as np
import matplotlib.pyplot as plt



#Plotting all lines
x = np.linspace(-10, 10, 40)
y1=2*x-1
y2 =0.06*x+2.88
y3=-1.52*x+6.04
plt.plot(x,y1, label ='-2x+y=1')
plt.plot(x,y2, label = '-0.06x+y=2.88')
plt.plot(x,y3, label = '1.52x+y=6.04')
plt.plot(2, 3, 'ro', label = 'intersection point(2,3)')
plt.xlim(-8,8)
plt.ylim(-9,9)
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() 
plt.savefig('plot.png')
#plt.show()
