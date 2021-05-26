

#Drawing a triangle DEF
 
import numpy as np
import matplotlib.pyplot as plt
 
 
 
#Sides
DE = 5
DF= 3
 
 
#Calculating third side 
EF=((DE*DE)+(DF*DF))
 
#Triangle vertices
D= np.array([0,0]) 
E= np.array([0,DE]) 
F = np.array([DF,0]) 
 
 
#Generating all lines
x_DE = line_gen(D,E)
x_DF = line_gen(D,F) 
x_EF = line_gen(E,F)
 
#Plotting all lines
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_DF[0,:],x_DF[1,:],label='$DF$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')
 
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.1), E[1] * (1 - 0.1) , 'E')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.2), D[1] * (1) , 'D')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')
 
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
