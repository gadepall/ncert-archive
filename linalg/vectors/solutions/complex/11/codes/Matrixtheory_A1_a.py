import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10,10,100)
y1 = -x1


plt.plot(x1, y1, '-b')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.title('Part(a)')
plt.axhline()
plt.axvline()

plt.grid()
plt.show()