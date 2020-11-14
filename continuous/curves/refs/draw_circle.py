#Code by GVV Sharma
#March 26, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

#Plotting the circle
c = 6
theta = np.linspace(0,2*np.pi,50)
x = c*np.cos(theta)
y = c*np.sin(theta)

plt.plot(x,y)

plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#if using termux
plt.savefig('../figs/circle.pdf')
plt.savefig('../figs/circle.eps')
subprocess.run(shlex.split("termux-open ../figs/circle.pdf"))
#else
#plt.show()







