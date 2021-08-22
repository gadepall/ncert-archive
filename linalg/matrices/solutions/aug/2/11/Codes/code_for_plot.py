import matplotlib.pyplot as plt
import numpy as np

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from coeffs import *

x = np.linspace(-10,10,500);
y1 = 2*x-10;
plt.plot(x, y1, 'r', label = '2x-y = 10')

y2 = 5-3*x;
plt.plot(x, y2, 'c',label = '3x+y = 5');
plt.title('Intersection of two straight lines', fontsize=10)
plt.annotate("solution (3,-4)", (3,-4))

plt.xlabel('x-axis');plt.ylabel('y-axis')
plt.legend(loc='best');plt.grid()
plt.savefig('../figures/Plot.png')