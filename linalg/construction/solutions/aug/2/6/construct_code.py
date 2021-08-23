## Author: Ganji Varshitha (AI20BTECH11009) ##
## Code to plot quadrilateral ##
#importing numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

## quadrilateral LIFT LI = 4, IF = 3, TL = 2.5, LF = 4.5, IT = 4
## Considering triangles LIF,LIT
# triangle LIF sides
a=4
b=3
c=4.5
print('Coordinates of L: 0 0')
print('Coordinates of I: 4 0')
## Vertices L,I 
L = np.array([0,0]) 
I = np.array([a,0])

## Coordinates of F
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print('Coordinates of F:',p,q)


F = np.array([p,q]) 
 

# triangle LIT sides
a=4
b=4
c=2.5
## Coordinates of T
p1 = (a**2 + c**2-b**2 )/(2*a)
q1 = np.sqrt(c**2-p1**2)
print('Coordinates of T:',p1,q1)

T = np.array([p1,q1]) 

#Plotting
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.1), F[1] * (1 - 0.1) , 'F')
plt.plot(L[0], L[1], 'o')
plt.text(L[0] * (1 - 0.2), L[1] * (1) , 'L')
plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 + 0.03), I[1] * (1 - 0.1) , 'I')
plt.plot(T[0], T[1], 'o')
plt.text(T[0] * (1 + 0.1), T[1] * (1 - 0.1) , 'T')

plt.plot(np.array([p,0]),np.array([q,0]), 'b', label="$FL$")
plt.plot(np.array([0,4]), np.array([0,0]),'r', label="$LI$")
plt.plot(np.array([4,p]), np.array([0,q]),'g', label="$IF$")
plt.plot(np.array([4,p1]), np.array([0,q1]),'c', label="$IT$")
plt.plot(np.array([0,p1]), np.array([0,q1]),'m', label="$LT$")
plt.plot(np.array([p1,p]), np.array([q1,q]),'y', label="$TF$")



plt.grid()
plt.xlim(-1,10)
plt.ylim(-1,5)
plt.legend(loc='lower right')
plt.show()

