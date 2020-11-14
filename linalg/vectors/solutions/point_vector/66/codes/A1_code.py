import numpy as np
import matplotlib.pyplot as plt
class point:

  def __init__(self,x_val,y_val,z_val):
    self.x = x_val
    self.y = y_val
    self.z = z_val

def check(p1,p2):
 
  # Direction vector for Line 1
  A = [p1.x +p2.x , p1.y+p2.y , p1.z+p2.z]
  # Direction vector for Line 2
  B = [p1.x -p2.x, p1.y - p2.y, p1.z -p2.z]
  print("Direction Vector for Line 1: {}i+{}j+{}k".format(A[0],A[1],A[2]))
  print("Direction Vector for Line 2: {}i+{}j+{}k".format(B[0],B[1],B[2]))
  #plt.plot(A)
  #plt.plot(B)
  #plt.xlim(0,2)
  #plt.legend()
  
  if (np.dot(A,B)==0):
    return "Perpendicular"
  elif (sum(np.cross(A,B))==0):
    #Satisfies the condition for being parallel
    return "Parallel"
  else:
    #Neither parallel nor perpendicular
    return "Neither Parallel nor Perpendicular"

# Driver Code
# Line 1
P1 = point(5,-1,-3) 
P2 = point(1,3,-5)
print ("The lines through the given points are : {}".format(check(P1,P2)))