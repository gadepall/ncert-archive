import pulp
from pulp import *
import pandas as pd
import numpy as np
from coeffs import *
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

A = np.array(([1.0,2.0],[1.0,1.0],[1.0,-2.0]))
b = np.array([ 120.0, 60.0 ,0.0]).reshape((3,1))
c = np.array([ 5.0, 10.0 ])
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
for i in range(0,1):
    model+=lpSum((A[i][j]*x1[j]) for j in range(0,2)) <= b[i]
print("\n",model)
for i in range(1,3):
    model+=lpSum((A[i][j]*x1[j]) for j in range(0,2)) >= b[i]
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


#Model initialization
model = LpProblem("Minimization-Problem", LpMinimize)

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
for i in range(0,1):
    model+=lpSum((A[i][j]*x1[j]) for j in range(0,2)) <= b[i]
print("\n",model)
for i in range(1,3):
    model+=lpSum((A[i][j]*x1[j]) for j in range(0,2)) >= b[i]
print("\n",model)

model.writeLP("Minimization-Problem.lp")
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
print("Minimum value of Z=",value(obj_func))