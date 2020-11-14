#taking the three given vectors as a,b,c
import numpy as np

a=np.array([2/7,3/7,6/7])
b=np.array([3/7,-6/7,2/7])
c=np.array([6/7,2/7,-3/7])

print("magnitude of vector a is :")
print(np.linalg.norm(a))

print("magnitude of vector b is :")
print(np.linalg.norm(b))

print("magnitude of vector c is :")
print(np.linalg.norm(c))

#when two vectors are perpendicular their dot product is zero

#Multiplied by a scalar(7) to increase precision 
print("The dot product of a and b is :")
print(np.dot(np.multiply(7,a),np.multiply(7,b)))

print("The dot product of b and c is :")
print(np.dot(np.multiply(7,c),np.multiply(7,b)))

print("The dot product of c and a is :")
print(np.dot(np.multiply(7,a),np.multiply(7,c)))
