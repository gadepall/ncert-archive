import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10,10,100)
y1 = -((np.sqrt(2)/np.sqrt(3))*x1)

x2 = np.linspace(-10,10,100)
y2 = -((np.sqrt(3)/np.sqrt(8))*x2)

plt.plot(x1, y1, '-r')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.plot(x2, y2, '-b')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')

plt.title('Part(e)')


plt.grid()
plt.show()