import numpy as np
from scipy.stats import binom
from math import comb
simlen=int(1e6)
#binomial parameters 
pp=1/3
nn=4
#calculation of theoritical probability of a binomial distribution
def prob(n,k,p):
	prob=comb(n,k)*(p**k)*((1-p)**(n-k))
	return(prob)
mean=0
#calculating mean
for i in range(0,5):
	mean=mean+i*prob(nn,i,pp)
#Simulations using Bernoulli r.v.
data_bin = binom.rvs(n=nn,p=pp,size=simlen)


#Theory vs simulation
print(mean,np.mean(data_bin))









