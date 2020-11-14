#Program to plot cosine function using matplotlib. 

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi, 0.1)
y = np.cos(x)

plt.plot(x,y)
plt.xlabel('X values from 0 to 2*pi')
plt.ylabel('Cos(x) values')
plt.title('Cosine Function')

y = 0.5
x = np.arccos(y)

plt.scatter(x,y,s=100, color = 'r')
plt.show()

