import numpy as np
from numpy import linalg
import math
#defining normal vectors
n1=np.array([[-2],[1]])      #subscript 1 for line with slope 2
n2a=np.array([[-0.06],[1]])  #subscript 2a for line with slope 0.06
n2b=np.array([[1.52],[1]])   #subscript 2b for line with slope -1.52

#finding transpose of normal vector
n1T=n1.T

#dot product of normal vectors
numa=np.dot(n1T,n2a)
numb=np.dot(n1T,n2b)

#finding magnitude of the vectors
modn1=linalg.norm(n1)
modn2a=linalg.norm(n2a)
modn2b=linalg.norm(n2b)

#calculating the cosine of angle between the lines
cosxa=numa/(modn1*modn2a)

#converting radians to degrees
#if clause to find out the acute angle
anglea=math.degrees(np.arccos(cosxa))
if anglea>90:
 print('angle between the line of slope 2 and 0.06 is', 180-anglea ,'degrees')
else:
 print('angle between the line of slope 2 and 0.06 is', anglea, 'degrees')
cosxb=numb/(modn1*modn2b)
angleb=math.degrees(np.arccos(cosxb))
if angleb>90:
 print('angle between the line of slope 2 and -1.52 is', 180-angleb, 'degrees')
else:
 print('angle between the line of slope 2 and -1.52 is', angleb, 'degrees')
