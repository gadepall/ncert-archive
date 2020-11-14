import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10,10,100)
y1 = x1-3

x2 = np.linspace(-10,10,100)
y2 = 12-((2/3)*x2)

plt.plot(x1, y1, '-r', label='(1 -1)x=3')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.plot(x2, y2, '-b', label='(1/3 1/2)x=6')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')

plt.title('Part(b)')


plt.grid()
plt.show()