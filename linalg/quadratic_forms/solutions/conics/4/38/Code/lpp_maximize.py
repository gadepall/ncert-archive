# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:38:27 2020
@author: Rubeena
"""

import pulp
from pulp import *
import pandas as pd
import numpy as np
from coeffs import *
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

A = np.array(([1.0,1.0],[3.0,1.0]))
b = np.array([ 50.0, 90.0 ]).reshape((2,1))
c = np.array([ 4.0, 1.0 ])
print("A=\n",A)
print("B=\n",b)
print("c=\n",c)

#Model initialization
model = LpProblem("Maximization-Problem", LpMaximize)

#Decision Variables

variable_names = [str(i+1) for i in range(0,2)]
variable_names.sort()
variable_names
DV_variables = LpVariable.matrix('X',variable_names , cat = "Integer" , lowBound= 0 )
x1=np.array(DV_variables)

#Objective
obj_func = c@x1
model +=  obj_func

#Constraints
for i in range(0,2):
    model+=lpSum((A[i][j]*x1[j]) for j in range(0,2)) <= b[i]  
print("\n",model) 

model.writeLP("Maximization-Problem.lp")
model.solve()
status =  LpStatus[model.status]
print(status)

for v in model.variables():
    try:
        print(v.name,"=", v.value())
    except:
        print("error couldnt find value")

#Final Solution
print("Printing the final solution:\n")  
for i in range (0,2):
    print("X_",i+1,"=",value(x1[i])) 
print("Maximum value of Z=",value(obj_func))

#Line Parameters
n1 = np.array([A[0][0],A[0][1]])
n2 = np.array([A[1][0],A[1][1]])

#Equation of lines
c1 = 50
c2 = 90
e1 = np.array([1,0])
e2 = np.array([0,1])
[A,B]=line_icepts(n1, c1)
[C,D]=line_icepts(n2, c2)

x1=np.linspace(-20,60,100)
y1=(c1*np.ones(100) - x1)
x2=np.linspace(-20,60,100)
y2=(c2*np.ones(100) - 3*x1)
P=line_intersect(n1,c1,n2,c2)
O=line_intersect(n1, 0, n2, 0)

#Plotting Lines
plt.plot(x1,y1,label='$1$')
plt.plot(x2,y2,label='$2$')
plt.axhline(y=0,color='r',label='$3$')
plt.axvline(x=0,color='g',label='$4$')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1+0.1), P[1], 'P')
plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1), A[1]*(1+0.03), 'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1+0.1), B[1], 'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1+0.1), C[1]*(1+0.1), 'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0], D[1], 'D')
plt.plot(O[0],O[1],'o')
plt.text(O[0], O[1], 'O')
plt.xlim(-50,100)
plt.ylim(-10, 100)
plt.legend(loc='best')
plt.grid() # minor

plt.show()