# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 02:50:49 2020

@author: Rubeena
"""


import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #Taken from Dr. G.V.V's github

#Line points
P = np.array([1,2]) 
Q = np.array([5,3]) 
A = np.array([2.6,0])  #thepoint on x-axis where reflection takes place
normal=np.array([1,0])


inc_PA=(P-A) #incident vector
ref_QA=Q-A #reflected vector

angle_inc=(np.transpose(inc_PA)@normal)/(np.linalg.norm(inc_PA))
angle_ref=np.transpose(ref_QA)@normal/(np.linalg.norm(ref_QA))

print("cosine of angle of incidence=")
print(angle_inc)
print("\n")
print("cosine of angle of reflection=")
print(angle_ref)
print("\n")
#reflected_ray=inc_PA-2*((np.transpose(inc_PA))@normal)*normal #ref=inc-2(transpose(inc)*normal)*normal
#print(reflected_ray)

print(inc_PA)
print("\n")
print(ref_QA) #we need to check if unit vector ref_QA and reflected_ray a are same


#Draw figure for reflection

x_PA=line_gen(P,A)
plt.plot(x_PA[0,:],x_PA[1,:],label="PA")

x_QA=line_gen(Q,A)
plt.plot(x_QA[0,:],x_QA[1,:],label="QA")

#plotting and labelling of points
plt.plot(P[0], P[1], '.')
plt.text(P[0] * (1 + 0.1), P[1] * (1 + 0.1) , 'P(1,2)')
plt.plot(Q[0], Q[1], '.')
plt.text(Q[0] * (1 -0.06), Q[1] * (1+0.05) , 'Q(5,3)')
plt.plot(A[0], A[1], '.')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(13/5,0)')


plt.grid()
plt.xlim(0, 6)
plt.ylim(-1, 6)



