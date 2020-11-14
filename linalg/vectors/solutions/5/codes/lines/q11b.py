import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = np.linspace(-5,5,5)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#plt.plot(x, -x, '-r', label='A')
plt.plot(x, 2*x+1,'g', label='D')
#plt.plot(x, 2*x,'b', label='B')
plt.plot(x, 2*x-4,'m', label='E')
#plt.plot(x, x,'y', label='C')
plt.plot(x, x-4,'violet', label='F')
plt.grid()
#plt.axis('equal')
plt.legend(loc='upper left')

plt.savefig('./figs/q11b.pdf')
plt.savefig('./figs/q11b.eps')
plt.show()


