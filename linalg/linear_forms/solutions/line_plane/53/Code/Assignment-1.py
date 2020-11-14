import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
# Create the vectors X and Y
x1 = np.linspace(-5,5,300)
y1 = (4 - x1)


P1= np.array([4, 0])
Q1 = np.array([0, 4])

# Create the plot
plt.plot(x1,y1,label='x+y=4')
plt.axhline(y=2,label='y=2')
plt.axvline(x=-1,label='x=-1')

plt.plot(P1[0],P1[1],'o')
plt.text(P1[0]*(1+0.1), P1[1]*(1-0.1), 'P1')
plt.plot(Q1[0],Q1[1],'o')
plt.text(Q1[0]*(1-0.2), Q1[1]*(1), 'Q1')

plt.title('lines and planes ')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')

# Add a Legend
plt.legend()
#plt.savefig('../figures/line/lines_and_planes/lines_and_planes.eps')
# Show the plot


A = np.array([3,1])
m = np.array([1,-1])
B = np.array([-1,2])


plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1), A[1]*(1-0.1), 'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.2), B[1]*(1), 'B')
lambda1=-4
#First Intersection Point: X1=A+lambda1*M
x1 = np.add(A,lambda1*m)

# Direction Vector_1: V1=B-X1
v1 = np.subtract(B,x1)

lambda2=-1
#Second Intersection Point: X2=A+lambda2*M
x2 = np.add(A,lambda2*m)

# Direction Vector_2: V2=B-X2
v2 = np.subtract(B,x2)

print("Intersection Points:")
print(x1, x2)
print("Direction Vectors:")
print(v1, v2)

plt.show()
