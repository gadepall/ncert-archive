import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-15,15,10)
A = np.array([[12,-5],[5,12]])     
B = np.array([[-82],[-7]])           # constants
C = np.dot(np.linalg.inv(A),B)       # getting the point of intersection
a   = C[0]
b   = C[1]
p1  = (1,-1)                         # given point
p2  = (a,b)                          # reading the points of intersection into P2
d   = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ) #getting the distance
y1  = ((12*x)+82)/5

x2 = [p1[0], p2[0]]
y2 = [p1[1], p2[1]]

print (a,b)
print (d)
plt.plot(x,y1, label = '(12 -5)x = -82')
plt.plot(x2,y2, label = 'distance = 99/13')

plt.plot(p1[0], p1[1], 'g*',label = 'point (1,-1)')
plt.axis("equal")

plt.xlim(-9,9)
plt.ylim(-5,5)
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid() 

