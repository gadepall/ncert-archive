import numpy
  
u = numpy.array([1, 3, 7])  
v = numpy.array([7, -1, 8])    
  
v_mag = numpy.sqrt(sum(v**2))       # To calculate the magnitude of vector v.  
p= (numpy.dot(u, v)/v_mag**2)*v     # To calculate the projection of u on v.
  
print("Projection of Vector u on Vector v is: ", p)
#Output : Projection of Vector u on Vector v is:  [ 3.68421053 -0.52631579  4.21052632]
