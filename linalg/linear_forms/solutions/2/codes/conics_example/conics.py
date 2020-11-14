import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


# equation - x^2 - 2*x
X_coord = np.array(np.linspace(-2.0, 4.0, num=40))
Y_coord =  [num**2 - 2*num for num in X_coord]

#plot points and lines
plt.plot(X_coord, Y_coord, label='$x^2 - 2x$')
plt.plot(findingRoots(1, -2, 0)[1], 0, 'o', label='$x_1$')
plt.plot(findingRoots(1, -2, 0)[0], 0, 'o', label='$x_2$')
plt.text(findingRoots(1, -2, 0)[0] * (1 + 0.1), 0, '$x_2$')
plt.text(findingRoots(1, -2, 0)[1] + 0.3, 0, '$x_1$')


plt.axis('equal')
plt.legend(loc='best')
plt.grid()

# if using termux
# plt.savefig('./figs/quadratic_equation.pdf')
# plt.savefig('./figs/quadratic_equation.eps')
# subprocess.run(shlex.split("termux-open ./figs/quadratic_equation.pdf"))
# else
plt.show()
