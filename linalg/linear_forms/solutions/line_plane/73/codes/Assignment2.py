
import numpy as np

import math
vector_1 = [3,2,6] #Direction vector of first line in problem 1
vector_2 = [1,2,2] #Direction vector of second line in problem 1
vector_3 = [1,-1,-2] #Direction vector of first line in problem 2
vector_4 = [3,-5,-4] #Direction vector of second line in problem 2

unit_vector_1 = vector_1 / np.linalg.norm(vector_1) #Calculating unit vector of vector1
unit_vector_2 = vector_2 / np.linalg.norm(vector_2) #Calculating unit vector of vector2
unit_vector_3 = vector_3 / np.linalg.norm(vector_3) #Calculating unit vector of vector3
unit_vector_4 = vector_4 / np.linalg.norm(vector_4) #Calculating unit vector of vector4
dot_product1 = np.dot(unit_vector_1, unit_vector_2) #calculating dot product of unit vector 1 and 2
dot_product2 = np.dot(unit_vector_3, unit_vector_4) #calculating dot product of unit vector 3 and 4
angle1 = np.arccos(dot_product1) * 180 / math.pi #calculating angle between of unit vector 1 and 2
angle2 = np.arccos(dot_product2) * 180 / math.pi #calculating angle between of unit vector 3 and 4
print("Problem (1) - Angle between L1 and L2 is : ", angle1)
print("Problem (2) - Angle between L1 and L2 is : ", angle2)


	





