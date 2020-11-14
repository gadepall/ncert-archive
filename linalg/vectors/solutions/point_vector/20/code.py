import numpy as np
class point:
  '''
  A class for 3 Dimensional Points
  '''
  def __init__(self,x_val,y_val,z_val):
    self.x = x_val
    self.y = y_val
    self.z = z_val

def check(p1,p2,p3,p4):
  '''
  A function to check wheather two lines are parallel or perpendicular 
  Args : p1,p2,p3,p4 (point objects) where p1,p2 belongs to the first line and p3,p4 belongs to the second line.
  returns: "Parallel", "Perpendicular" and "Neither Parallel nor Perpendicular"
  '''
  # Direction vector for Line 1
  A = [p2.x - p1.x, p2.y - p1.y , p2.z - p1.z]
  # Direction vector for Line 2
  B = [p4.x - p3.x, p4.y - p3.y , p4.z - p3.z]

  print("Direction Vector for Line 1: {}i+{}j+{}k".format(A[0],A[1],A[2]))
  print("Direction Vector for Line 2: {}i+{}j+{}k".format(B[0],B[1],B[2]))

  if (np.dot(A,B)==0):
    "Satisfies the condition for being perpendicular"
    return "Perpendicular"
  elif (sum(np.cross(A,B))==0):
    "Satisfies the condition for being parallel"
    return "Parallel"
  else:
    "Neither parallel nor perpendicular"
    return "Neither Parallel nor Perpendicular"

# Driver Code

# Line 1
P1 = point(1,-1,2) 
P2 = point(3,4,-2)

# Line 2
P3 = point(0,3,2)
P4 = point(3,5,6)

print ("The lines through the given points are : {}".format(check(P1,P2,P3,P4)))