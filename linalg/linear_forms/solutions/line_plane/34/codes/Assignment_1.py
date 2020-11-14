import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(-10,10,1000)
x2 = (12*np.ones(1000) - 4*x1)/3

x3 = np.linspace(-10,10,1000)
x4 = (32*np.ones(1000) - 4*x3)/3

x5 = np.linspace(-10,10,1000)
x6 = (-8*np.ones(1000) - 4*x5)/3

x9 = np.linspace(-10,10,1000)
x10 = (6*np.ones(1000) + 3*x9)/4

x11 = np.linspace(-10,10,1000)
x12 = (-24*np.ones(1000) + 3*x11)/4



x8 = np.zeros(100)
x7 = np.linspace(-10,10,100)

plt.plot(8,0,'o',label = "(8,0)")
plt.plot(-2,0,'o',label = "(-2,0)")
plt.plot(3,0,'o',label = "(3,0)")
plt.plot(x1,x2)
plt.plot(x3,x4)
plt.plot(x5,x6)
plt.plot(x7,x8)
plt.plot(x9,x10)
plt.plot(x11,x12)
plt.ylim(-10, 10)
plt.grid()
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()