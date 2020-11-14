import numpy
A = numpy.array([[3,2],[1,1]])
I = numpy.array([[1,0],[0,1]])
A_2 = numpy.matmul(A,A)
L = A_2-4*A+I
print("A = ")
print(A)
print("A^2-4A+I = ")
print(L)
