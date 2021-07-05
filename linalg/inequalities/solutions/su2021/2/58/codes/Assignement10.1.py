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

#Generating and plotting line x+2y=10
A=np.array([-2,6])
B=np.array([6,2])
AB=line_gen(A,B)
plt.plot(AB[0,:],AB[1,:],label='x+2y=10')

#Generating and plotting line x+y=1
C=np.array([3,-2])
D=np.array([-3,4])
CD=line_gen(C,D)
plt.plot(CD[0,:],CD[1,:],label='x+y=1')

#Generating and plotting line y=x
E=np.array([-1,-1])
F=np.array([4,4])
EF=line_gen(E,F)
plt.plot(EF[0,:],EF[1,:],label='y=x')


#Generating and plotting line x=0
E=np.array([0,-2])
F=np.array([0,6])
EF=line_gen(E,F)
plt.plot(EF[0,:],EF[1,:],label='x=0')

#Labelling points
plt.plot(3.33,3.33,'o',color='r')
plt.text(4,3.2,'B(10/3,10/3)')
plt.plot(0.5,0.5,'o',color='r')
plt.text(1,0.5,'C(1/2,1/2)')
plt.plot(0,1,'o',color='r')
plt.text(-1.5,1,'D(0,1)')
plt.plot(0,5,'o',color='r')
plt.text(0.5,5,'A(0,5)')


#Shading Required Region
x1=[0,3.33,0.5,0]
y1=[5,3.33,0.5,1]
plt.fill(x1,y1,color="gray",alpha = 0.3)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
