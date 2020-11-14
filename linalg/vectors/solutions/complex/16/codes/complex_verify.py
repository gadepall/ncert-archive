import numpy as np
import math
from numpy import linalg as LA

#print('Enter the vector')
a1=1
a2=1
m1=[[a1, -a2], 
    [a2, a1]]
print('m1=',m1)
print('len-m1=',len(m1))
p1=[[1], 
    [0]]

a3=1
a4=-1
m2 = [[a3, -a4], 
    [a4, a3]]
print('m2=',m2)

y1 = np.linalg.inv(m2)
print('y1=',y1)

y2 = np.linalg.inv(m1)
print('y2=',y2)


result1 = [[0,0],  
               [0,0]]  
 
 
for i in range(len(m1)):  
   for j in range(len(y1[0])):  
       for k in range(len(y1)):  
           result1[i][j] += m1[i][k] * y1[k][j]  
print(result1)  

result2 = [[0],  
               [0]]         

for i in range(len(result1)):  
   for j in range(len(p1[0])):  
       for k in range(len(p1)):  
           result2[i][j] += result1[i][k] * p1[k][j]  
print(result2) 



result3 = [[0,0],  
               [0,0]]  
 
  
for i in range(len(m2)):  
   for j in range(len(y2[0])):  
       for k in range(len(y2)):  
           result3[i][j] += m2[i][k] * y2[k][j]  
print(result3)

result4 = [[0],  
               [0]]         

for i in range(len(result3)):  
   for j in range(len(p1[0])):  
       for k in range(len(p1)):  
           result4[i][j] += result3[i][k] * p1[k][j]  
print(result4)  

#sub_result = result2 - result4
#print('sub_result',sub_result)


result5 = [[0],
         [0]]
         

for i in range(len(result2)):
   # iterate through columns
   for j in range(len(result2[0])):
       result5[i][j] = result2[i][j] - result4[i][j]
print(result5)

norm_result5 = LA.norm(result5)
print('normalized final result=',norm_result5)
