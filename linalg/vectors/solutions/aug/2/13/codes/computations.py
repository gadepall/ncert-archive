import numpy

A = numpy.array([1,-2,-8])
B = numpy.array([5,0,-2])
C = numpy.array([11,3,7])

print("Lambda= ",numpy.linalg.norm(B-A)/numpy.linalg.norm(C-B),"=2/3")

