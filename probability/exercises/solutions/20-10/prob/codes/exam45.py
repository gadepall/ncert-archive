import numpy as np
from scipy.stats import binom
from math import comb
simlen=int(1e6)
#binomial parameters 
k=0
p=3/4
minp=0.01
#calculation of theoritical probability of a binomial distribution
def prob(n,k,p):
	prob=comb(n,k)*(p**k)*((1-p)**(n-k))
	return(prob)
i=1
while(prob(i,k,p)>minp):
	i=i+1
print(i)
