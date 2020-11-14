import numpy as np
import matplotlib.pyplot as plt 


x_coordinates = [50,55,60,65,70,75]

y_coordinates = [100,98,90,78,54,16]


plt.scatter(x_coordinates, y_coordinates)

plt.plot(x_coordinates, y_coordinates)
plt.xlabel('Production yield')
plt.ylabel('No.of farms')
plt.grid()
plt.savefig('ex_q25.pdf')
plt.savefig('ex_q25.eps')
plt.show()
