import numpy as np 

#b = np.array([[6,1,1], [4, -2, 5], [2,8,7]]) 
#print (b) 
#c= np.linalg.det(b) 
#k= abs(c)
#print (c) 
#print (k)


## For ABC triangle

m = np.array([[4,-6,1], [3, -2, 1], [5,2,1]])
print (m) 
d1 = np.linalg.det(m) 
mod_d1= abs(d1)
#print (mod_d1)
area = 0.5* mod_d1
print ("Area of ABC triangle is :",area)


## For ABP triangle

n = np.array([[4,-6,1], [3, -2, 1], [4.5,-2,1]])
print (n) 
d2 = np.linalg.det(n) 
mod_d2= abs(d2)
#print (mod_d2)
A1 = 0.5* mod_d2
print ("Area of ABP triangle is :",A1)


## For ABN triangle

o = np.array([[4,-6,1], [3, -2, 1], [4,0,1]])
print (o) 
d3 = np.linalg.det(o) 
mod_d3= abs(d3)
#print (mod_d3)
A2 = 0.5* mod_d3
print ("Area of ABN triangle is :",A2)

## For CAM triangle

p = np.array([[4,-6,1], [5, 2, 1], [3.5,-4,1]])
print (p) 
d4 = np.linalg.det(p) 
mod_d4= abs(d4)
#print (mod_d4)
A3 = 0.5* mod_d4
print ("Area of CAM triangle is :",A3)


