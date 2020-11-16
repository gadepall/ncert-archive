import numpy as np
from scipy.stats import binom
from math import comb
simlen=int(1e6)
#binomial parameters 
k=0
pp=0.1
nn=10
#calculation of theoritical probability of a binomial distribution
def prob(n,k,p):
	prob=comb(n,k)*(p**k)*((1-p)**(n-k))
	return(prob)

#Simulations using Bernoulli r.v.
data_bin = binom.rvs(n=nn,p=pp,size=simlen)

#Calculating the number of favourable outcomes from the simulation
def fav(data_bin,k):
	err_ind = np.nonzero(data_bin !=k)
	err_n = np.size(err_ind)/simlen
	return(err_n)

#Theory vs simulation
print(fav(data_bin,k),1-prob(nn,k,pp))









