
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
frame1=plt.gca()
x=np.linspace(-3,5,80)
y=0*x
plt.axhline(y=0,xmin=0.5,xmax=1,linewidth=4,color='r')
plt.plot(x,y)
#plt.title('Graph of 3x-y=3')
plt.xlabel('$x$')
#plt.ylabel('$y$')
#plt.legend(loc='best')
#plt.grid() # minor
frame1.axes.get_yaxis().set_visible(False)
plt.savefig('./pyfigs/secondline.eps')

#print(3)
plt.show()
#print(4)




