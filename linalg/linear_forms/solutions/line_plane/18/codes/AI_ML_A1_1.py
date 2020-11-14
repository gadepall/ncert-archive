import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10,10,100)
y1 = 14-x1

x2 = np.linspace(-10,10,100)
y2 = x2-4

plt.plot(x1, y1, '-r', label='(1 1)x=14')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.plot(x2, y2, '-b', label='(1 -1)x=4')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')
plt.title('Part(a)')


plt.grid()
plt.show()