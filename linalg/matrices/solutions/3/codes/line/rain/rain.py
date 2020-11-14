
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#velocity of woman along east to west
v_w=-12
#velocity of rain vertically downwards
v_r=-35
#ends of the velocity vectors
A = np.array([v_w,0])
B =-A
C = np.array([0,v_r])
D=-C
O = np.array([0,0])
# relative velocity of rain wrt woman
Vrw=C-A


#Generating all lines
x_Vw = line_gen(O,A)
x_Vwn = line_gen(O,B)
x_Vrn = line_gen(D,O)
x_Vrw = line_gen(D,B)
#Plotting all lines
plt.plot(x_Vw[0,:],x_Vw[1,:],label='$Vw$')
plt.plot(x_Vwn[0,:],x_Vwn[1,:],label='$-Vw$')
plt.plot(x_Vrn[0,:],x_Vrn[1,:],label='$Vr$')
plt.plot(x_Vrw[0,:],x_Vrw[1,:],label='$Vr-Vw$')

plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 - 0.1), O[1] * (1 + 0.1) , 'O')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

plt.savefig('./pyfigs/rain.eps')

#print(3)
plt.show()
#print(4)



