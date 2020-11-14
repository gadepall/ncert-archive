
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,10,500);
y1 = -(5/2)*x + 2;
plt.plot(x, y1, 'r', label = '5x+2y = 4')

y2 =(5-7*x)/3;
plt.plot(x, y2, 'c',label = '7x+3y = 5');
plt.title('Intersection of two straight lines', fontsize=10)

plt.xlim(-9,9)
plt.ylim(-9,9)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.annotate("(2,-3)", (2, -3))
plt.scatter(2, -3, s=10)

plt.legend()
plt.grid()
plt.show()

