import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex

# equation - x+5
X_coord1 = np.array(np.linspace(-10.0, 0.0, num=40))
Y_coord1 =  [num + 5 for num in X_coord1]

# equation - x-5
X_coord2 = np.array(np.linspace(0.0, 10.0, num=40))
Y_coord2 =  [num - 5 for num in X_coord2]

# equation - 2x+5
X_coord3 = np.array(np.linspace(-5.0, 0.0, num=40))
Y_coord3 =  [2*num + 5 for num in X_coord3]

# equation - 3x-2
X_coord4 = np.array(np.linspace(-1.0, 2.0, num=40))
Y_coord4 =  [3*num - 2 for num in X_coord4]

# equation - 3x
X_coord5 = np.array(np.linspace(-2.0, 2.0, num=40))
Y_coord5 =  [3*num for num in X_coord5]



#plot points and lines

plt.plot(X_coord1, Y_coord1, label='$x + 5$')
plt.plot(finding_roots_linear(1, 5), 0, 'o')
plt.text(finding_roots_linear(1, 5), -1, '$x_1$')


plt.plot(X_coord2, Y_coord2, label='$x - 5$')
plt.plot(finding_roots_linear(1, -5), 0, 'o')
plt.text(finding_roots_linear(1, -5), -1, '$x_1$')

plt.plot(X_coord3, Y_coord3, label='$2x + 5$')
plt.plot(finding_roots_linear(2, 5), 0, 'o')
plt.text(finding_roots_linear(2, 5), -1, '$x_1$')

plt.plot(X_coord4, Y_coord4, label='$3x - 2$')
plt.plot(finding_roots_linear(3, -2), 0, 'o')
plt.text(finding_roots_linear(3, -2), -1, '$x_1$')

plt.plot(X_coord5, Y_coord5, label='$3x$')
plt.plot(finding_roots_linear(3, 0), 0, 'o')
plt.text(-1, -1, '$x_1$')

plt.axis('equal')
plt.legend(loc='best')
plt.grid()

# if using termux
# plt.savefig('./figs/final_eq.pdf')
# plt.savefig('./figs/final_eq.eps')
# subprocess.run(shlex.split("termux-open ./figs/final_eq.pdf"))
# else
plt.show()
