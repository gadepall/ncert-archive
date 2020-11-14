import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10,10,100)
y1 = (1.3/0.3)-((0.2/0.3)*x1)

x2 = np.linspace(-10,10,100)
y2 = (2.3/0.5)-((0.4/0.5)*x2)

plt.plot(x1, y1, '-r', label='(0.2 0.3)x=1.3')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.plot(x2, y2, '-b', label='(0.4 0.5)x=2.3')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')

plt.title('Part(c)')


plt.grid()
plt.show()