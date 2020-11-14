
import numpy as np

def skew(vector):

    if isinstance(vector, np.ndarray):
        vector = vector.tolist()

    return np.array([[0, -vector[2], vector[1]],
                     [vector[2], 0, -vector[0]],
                     [-vector[1], vector[0], 0]])


#Line points
A = np.array([-1,0.5,4])
B = np.array([1,0.5,4])
C = np.array([1,-0.5,4])
D = np.array([-1,-0.5,4])

#adjacent sides
AD = np.linalg.norm(A-D)
BA = np.linalg.norm(B-A)

#Area= product of adjacent sides
area = AD*BA
print("Area of rectangle=",area)

#Cross product
ar = np.linalg.norm(np.cross(A-D,B-A))
print("Cross product area=",ar)

#Skew symmetric matrix multiplication
#print(A-D)
Y = skew(A-D)
#print("Skew symmetric matrix :", Y)
area = np.linalg.norm(np.cross(Y,B-A))
print("Area of rectangle =" ,area)
