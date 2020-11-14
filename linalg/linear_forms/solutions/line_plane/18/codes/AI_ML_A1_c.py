import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10,10,100)
y1 = (3*x1)-3

x2 = np.linspace(-10,10,100)
y2 = ((9*x1)-9)/3

plt.plot(x1, y1, '-r', label='(3 -1)x=3')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.plot(x2, y2, '-b', label='(9 -3)x=9')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')

plt.title('Part(c)')


plt.grid()
plt.show()