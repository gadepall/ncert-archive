import numpy as np
import matplotlib.pyplot as plt

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generating and plotting line x+2y=240
A=np.array([240,0])
B=np.array([0,120])
AB=line_gen(A,B)
plt.plot(AB[0,:],AB[1,:],label='x+2y=240')

#Generating and plotting line x+0.5y=90
C=np.array([0,180])
D=np.array([90,0])
CD=line_gen(C,D)
plt.plot(CD[0,:],CD[1,:],label='x+0.5y=90')

#Generating and plotting line 1.5x+2y=310
E=np.array([0,155])
F=np.array([206.667,0])
EF=line_gen(E,F)
plt.plot(EF[0,:],EF[1,:],label='1.5x+2y=310')

#Shading Required Region
x1=[40,140,20]
y1=[100,50,140]
plt.fill(x1,y1,color='gray')

#Labelling points
plt.plot(40,100,'o',color='r')
plt.text(20,90,'A(40,100)')
plt.plot(140,50,'o',color='r')
plt.text(120,40,'B(140,50)')
plt.plot(20,140,'o',color='r')
plt.text(20,145,'C(20,140)')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
