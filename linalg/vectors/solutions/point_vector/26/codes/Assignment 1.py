from math import sqrt
import numpy
vector=[1,1,1]
vector=numpy.array([1,1,1])
x=1/sqrt(3) #this can be changed to work with other root
vector=vector*x
print(numpy.linalg.norm(vector))
