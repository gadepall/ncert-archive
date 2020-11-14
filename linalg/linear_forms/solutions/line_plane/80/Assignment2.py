import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a1=np.array([1,-2,3])
a2=np.array([1,-1,-1])
b1=np.array([-1,1,-2])
b2=np.array([1,2,-2])
b1_b2=np.transpose(np.array((b2,-b1))) 
print(b1_b2,"\n")           #This gives the matrix [b2 -b1]

x=np.array((b1 @ b1_b2, b2 @ b1_b2))        
print(x,"\n")

y=np.array((b1 @ (a1-a2),b2 @ (a1-a2)))  
print(y,"\n")              

result=np.linalg.solve(x,y) #This computes the value of s and t at which equations b1^T(p2-p1)=0 and b2^T(p2-p1)=0 holds true.       
print("s={}, t={}".format(result[0],result[1]),"\n") 

p1=a1+result[1]*b1          #p1, p2 are the end points of the shortest distance 'd'
p2=a2+result[0]*b2

print("Point P1 on line L1 is {}".format(p1))
print("Point P2 on line L2 is {}".format(p2),"\n")

print("Hence the shortest distance between the two skew lines is {}".format(np.linalg.norm(p2 - p1)))


fig = plt.figure()
fig.set_size_inches(10,10)
ax = fig.add_subplot(111, projection='3d')

x_1=np.array([11,-9])
y_1=np.array([-12,8])
z_1=np.array([23,-17])

x_2=np.array([11,-9])
y_2=np.array([19,-21])
z_2=np.array([-21,19])

x_3=np.array((p1[0],p2[0]))
y_3=np.array((p1[1],p2[1]))
z_3=np.array((p1[2],p2[2]))

ax.plot(x_1,y_1,z_1,color='green',label='line_1')
ax.plot(x_2,y_2,z_2,color='red',label='line_2')
ax.plot(x_3,y_3,z_3,color='blue',label='line_3')
ax.scatter(x_3,y_3,z_3,color='black')

ax.set_xlabel('X - axis')
ax.set_ylabel('Y - axis')
ax.set_zlabel('Z - axis')
plt.show()

"""Output : 
[[ 1  1]
 [ 2 -1]
 [-2  2]] 

[[ 5 -6]
 [ 9 -5]] 

[ -9 -10] 

s=-0.5172413793103448, t=1.0689655172413794 

Point P1 on line L1 is [-0.06896552 -0.93103448  0.86206897]
Point P2 on line L2 is [ 0.48275862 -2.03448276  0.03448276] 

Hence the shortest distance between the two skew lines is 1.4855627054164149"""
