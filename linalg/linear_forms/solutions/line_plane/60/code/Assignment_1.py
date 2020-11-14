import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #refered from G.V.V sir's code



#finding solution of two linear equation, this will give the foot of the perpendicular
A = np.array([[2, -3], [3, 4]])
B = np.array([[4], [5]])
pt=np.linalg.inv(A) @ B
print("Junction Point is",np.linalg.inv(A) @ B)  #this line prints the solution which is the foot of the perpendicular, the same values are used in variable P

#Plotting for showing the graph :

#Inputs
M = np.array([-1,-2]) #a point satisfying equation of given line
N = np.array([5,2])  # another point satisfying equation of given line
O = np.array([-1,2])  #a point satisfying equation of given line
P = np.array([7,-4]) #another point satisfying equation of given line

#Generating all lines
x_AB = line_gen(M,N)
x_CD = line_gen(O,P)



# Python3 implementation of the approach  
  
# Function to find foot of perpendicular  
# from a point in 2 D plane to a Line  
def findFoot(a, b, c, x1, y1):  
  
    temp = (-1 * (a * x1 + b * y1 + c) //
                  (a * a + b * b))  
    x = temp * a + x1  
    y = temp * b + y1  
    return (x, y)  

  
if __name__ == "__main__": 
  
    # Equation of line is  
    # ax + by + c = 0  
    a, b, c = 6, -7, 8
      
    # Coordinates of point p(x1, y1).  
    x1, y1 = pt[0], pt[1]
  
    foot = findFoot(a, b, c, x1, y1)  
#    print(int(foot[0]), int(foot[1]))  
          


# Function to find the line given two points  
def lineFromPoints(P,Q): 
  
    a1 = Q[1] - P[1] 
    b1 = P[0] - Q[0]  
    c1 = a1*(P[0]) + b1*(P[1])  
  
    if(b<0):  
        print("The line passing through points P and Q is:", 
              a1 ,"x ",b1 ,"y = ",c1 ,"\n")  
    else: 
        print("The line passing through points P and Q is: ", 
              a1 ,"x + " ,b1 ,"y = ",c1 ,"\n")  
  
# Driver code  
if __name__=='__main__': 
    P = pt 
    Q = foot
    lineFromPoints(P,Q)  

O = np.array([6,4])  #a point satisfying equation of given line
P = np.array([-1,-2]) #another point satisfying equation of given line
U = np.array([pt[0],pt[1]])  #a point satisfying equation of given line
V = np.array([foot[0],foot[1]]) #another point satisfying equation of given line
L = np.array([O[0],O[1]])  #a point satisfying equation of given line
M = np.array([P[0],P[1]]) #another point satisfying equation of given line

#Generating all lines
x_PQ= line_gen(U,V)
x_LM= line_gen(O,P)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='he should follow the path PQ')
plt.plot(x_LM[0,:],x_LM[1,:],label='$LM$')
plt.plot(pt[0],pt[1],label='Junction pt. AB')


plt.plot(M[0], M[1], 'o')
plt.plot(N[0], N[1], 'o')
plt.plot(O[0], O[1], 'o')
plt.plot(P[0], P[1], 'o')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
