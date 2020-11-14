import numpy as np
from matplotlib import pyplot as plt
def f(t):
    return 5-t

t = np.arange(-5,6)
plt.plot(t,f(t),'*-r')
#plt.plot(x_AD[0,:],x_AD[1,:],'*r',label='$AD$')

plt.fill_between(t,f(t))
#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()

#if using termux
plt.savefig('figs/q6.pdf')
plt.savefig('figs/q6.eps')
#subprocess.run(shlex.split("termux-open ./line/figs/line_ineq.pdf"))
#else
plt.show()
