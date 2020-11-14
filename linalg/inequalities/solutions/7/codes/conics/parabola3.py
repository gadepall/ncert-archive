import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-4,2,100)
p=np.poly1d([4,4*math.sqrt(3),3])
for i in range(len(x)):
    y=p(x)

roots=p.r
A=np.array([roots[0],0])
B=np.array([roots[1],0])
print(A,B)
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.5), B[1] * (1-0.1) , 'B')
plt.plot(x,y)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show() 
