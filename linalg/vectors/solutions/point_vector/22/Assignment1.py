# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:39:44 2020

@author: Rishab
"""

import matplotlib.pyplot as plt

a = [7,6]
b = [5,0] #The vector b is equidistant from vectors a and c. Obtained from calculation 
c = [3,4]

plt.plot(a[0],a[1],'o')
plt.text(7,6,'A')
plt.plot(b[0],b[1],'o')
plt.text(5,0,'B')
plt.plot(c[0],c[1],'o')
plt.text(3,4,'C')


x=[7,5,3]
y=[6,0,4]

plt.plot(x,y,'ro')

def connect(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

connect(x,y,0,1)
connect(x,y,1,2)

plt.axis('equal')
plt.show()
