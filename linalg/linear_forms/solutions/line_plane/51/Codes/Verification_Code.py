import numpy as np
import math
from fractions import Fraction

#defining points A and B
A=np.array([(-1),(1)])
B=np.array([(5),(7)])

#n vector
nT=np.array([1,1])
n=np.transpose(nT)


#nTx=c line equation
x=np.array([(1),(3)])
c=np.dot(nT,x)

#expression of k
k=(np.subtract(np.dot(nT,A),np.dot(nT,x)))/(np.subtract(np.dot(nT,x),np.dot(nT,B)))
print(Fraction(k))
