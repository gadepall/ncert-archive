import numpy as np
import matplotlib.pyplot as plt
p = np.linspace(-10, 10, 20)
q1 =3*p-7
q2=-.33*p+3
q3=.5*p-1.5
plt.plot(p,q1, label = '-3x+y=-7')
plt.plot(p,q2, label = '1/3x+y=3')
plt.plot(p,q3, label = 'x-2y=3')
plt.plot(3, 2, 'ro', label = '(3,2)')
plt.xlim(-2,10)
plt.ylim(-7,7)
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.show()
