#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def parab_gen(y,a):
    x = y**2/a
    return x

omat = np.array([[0,1],[-1,0]]) 
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-3,3,len)

def line_dir_pt(m,A,k1,k2):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(k1,k2,len)
    for i in range(len):
        temp1 = A + lam_1[i]*m
        x_AB[:,i]= temp1.T
    return x_AB

#parab parameters
V = np.array(([1,0],[0,0]))
u = np.array(([-2,-1/2]))
ut = u[np.newaxis, :].T
f = 4
p = np.array(([0,1]))
p1t = p[np.newaxis, :].T
foc = np.abs(p@u)*2

# Eigenvalues and eigenvectors
# D_vec,P = LA.eig(V)
# D = np.diag(D_vec)
# print(D,P)
P = np.array(([0,1],[1,0]))
#Generating the Standard parabola
x = parab_gen(y,foc)
# y =(x-2)**2
# xStandardparab = np.vstack((x,y))
#
#Affine Parameters
R =  np.array(([0,1],[1,0]))
eta = (u@p1t)[0]
# print("eta",eta)
cA = np.vstack((u+(eta*p),V))
cb = np.vstack((-f,(eta*p1t-ut).reshape(-1,1)))
# print(cA)
# print(cb)
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()
xStandardparab = np.vstack((x,y))
xActualparab = P@xStandardparab + c[:,np.newaxis]
#
#Tangent Analysis
sec1 = np.array(([4,4]))
sec2 = np.array(([2,0]))
m = (sec1-sec2)/2
n = omat@m
kappa = p@u/(p@n)

qA = np.vstack((u+kappa*n,V))
qb = np.vstack((-f,(kappa*n-u).reshape(-1,1)))
q = LA.lstsq(qA,qb,rcond=None)[0]
q = q.flatten()

#Generating the tangent
k1 = 2
k2 = -2
x_AB = line_dir_pt(m,q,k1,k2)
#
#Generating the secant
x_sec12 = line_dir_pt(m,sec1,k1,k2)
#Labeling the coordinates
parab_coords = np.vstack((q,sec1,sec2)).T
plt.scatter(parab_coords[0,:], parab_coords[1,:])
vert_labels = ['$q$','$A$','$B$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='Tangent')

#Plotting all lines
plt.plot(x_sec12[0,:],x_sec12[1,:],label='Secant')

#Plotting the actual parabola
# plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='Parabola',color='y')
plt.plot(xActualparab[0,:],xActualparab[1,:],label='Parabola',color='r')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()

