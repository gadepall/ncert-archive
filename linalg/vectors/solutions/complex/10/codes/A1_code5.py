import numpy as np
X = np.array([[27,-414],[414,27]]);

Y = np.array([[5,1],[-1,5]]);

# resultant matrix
result = [ [0,0],[0,0]]

my_list = []
# iterating rows of X matrix
for i in range( len(X) ):
   # iterating columns of Y matrix
   for j in range(len(Y[0])):
       # iterating rows of Y matrix
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
  

for r in result:
   print(r)