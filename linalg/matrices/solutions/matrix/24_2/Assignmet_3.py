import numpy as np
M = [[1,2,3],[0,1,0],[1,1,0]]
N = [[-1,1,0],[-1,1,0],[2,3,4]]
result=np.dot(M,N)
result1=np.dot(N,M)
compare = result == result1
result3 = compare.all()
if result3!="true":
    print("Non Commutative")
