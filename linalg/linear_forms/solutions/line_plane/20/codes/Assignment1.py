#! /usr/bin/python3
import numpy as np

a=5
b=1
p = a-b
q= a+b
r = 3*a+b-2
full_rank=2
a = np.array([[2,3],
            [p,q]])  #Coefficient Matrix                
b = np.array([[7],[r]])
c = np.concatenate((a,b), axis=1)     #Augmented Matrix

Rank_A=np.linalg.matrix_rank(a)
Rank_B=np.linalg.matrix_rank(c)    
#print(Rank_A)
#print(Rank_B)
#For Infinite  solution if rank(Coefficient matrix)  equal to rank(Augmented matrix) and it should be less than full rank
if ((Rank_A == Rank_B)<(full_rank)):
    print("Infinite solution" )
