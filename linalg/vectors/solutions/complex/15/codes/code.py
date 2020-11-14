import numpy as np

#defining the equivalent matrices for complex numbers
A=np.array([[3,-5],[5,3]])
B=np.array([1,0])
C=np.array([[-6,-24],[24,-6]])

#calculating x and y values
Ainv=np.linalg.inv(a)
D=C@Ainv@B
x= D.T[0]
y=-D.T[1] 
print("x=" , x , "y=" ,y)

#proving conjugacy using x,y values obtained
X=np.array([[x,y],[-y,x]])
arr=np.array([-6,-24])
print("Conjugate of  ", arr , "is" , (X@A@B).T)
