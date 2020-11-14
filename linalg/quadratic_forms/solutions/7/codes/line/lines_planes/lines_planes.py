import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,10,100)
y = (x-4)/2

plt.plot(x, y, '-r', label='y=(x-4)/2')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
