import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10,10,100)
y1 = (0.9*x1)+1.2

x2 = np.linspace(-10,10,100)
y2 = (13/3)-((2/3)*x2)

plt.plot(x1, y1, '-r', label='(3/2 -5/3)x=-2')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.plot(x2, y2, '-b', label='(1/3 1/2)x=13/6')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')

plt.title('Part(f)')


plt.grid()
plt.show()