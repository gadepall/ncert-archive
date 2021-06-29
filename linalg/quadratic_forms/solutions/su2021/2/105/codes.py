import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/storage/emulated/0/tlc/school/ncert/linman/codes/CoordGeo')        #path to my scripts

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 5
y = np.linspace(-4,4,len)

#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

#def line_dir_pt
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#parab parameters
V = np.array(([1,0],[0,0]))
u = np.array(([0,-2/3]))
f = 0
#p = np.array(([1,0]))
#foc = np.abs(p@u)/2

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
p = P[:,0]
eta = 2*u@p
#foc = np.abs(eta/D_vec[1])
foc = -eta/D_vec[1]

#Affine Parameters
#c1 = np.array(([-(u@V@u-2*u@u+f)/(2*u@p),0]))
#c = -P@u+c1
#print(c1)
#p = -p
#cA = np.vstack((u+eta*p,V))
#cb = np.vstack((-f,(eta*p-u).reshape(-1,1)))
cA = np.vstack((u+eta*p*0.5,V))
cb = np.vstack((-f,(0.5*eta*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()
print(c,0,0,foc)
#print(cA,cb)
#print(p,c)


#Secant Analysis
sec1 = np.array(([-2,3]))
sec2 = np.array(([4,12]))
m = sec1-sec2
n = omat@m
#print(n)
kappa = p@u/(p@n)
#
qA = np.vstack((u+kappa*n,V))
qb = np.vstack((-f,(kappa*n-u).reshape(-1,1)))
q = LA.lstsq(qA,qb,rcond=None)[0]
q = q.flatten()
O = np.array([0,0])
print(c,q)
#
##Generating the secant
k1 = 2
k2 = -2
x_AB = line_dir_pt(m,q,k1,k2)

#Labeling the coordinates
parab_coords = np.vstack((q,sec1,sec2)).T
plt.scatter(parab_coords[0,:], parab_coords[1,:])
vert_labels = ['$C$','$K$','$L$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#Generating the Standard parabola
x = parab_gen(y,foc)
#y =(3*x*x)/4
xStandardparab = np.vstack((x,y))

#coordinates of each point
n = np.array([-2,0])
m = np.array([4,0])

#plotting points
plt.plot(m[0], m[1], 'o',color='b')
plt.text(m[0] + 0.3, m[1] + 0.3, 'M')
plt.plot(n[0], n[1], 'o',color='orange')
plt.text(n[0] - 1.3, n[1] + 0.3, 'N')

#Plotting all lines
plt.axhline(y=0,color='gray')
plt.plot(x1, y1, '-', label='$2y = 3x+12$',color='g')
plt.axvline(x=4,color='blue',label = 'x=4' ,linestyle='--')
plt.axvline(x=-2,color='orange',label ='x=-2',linestyle='--')

#Plotting the actual parabola
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='3x^2 = 4y',color='r')

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
