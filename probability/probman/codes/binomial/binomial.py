#Code by GVV Sharma
#November 20,2020
#Released under GNU/GPL
#To find the probability of an event using the binomial distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import binom




#Simlen
simlen=1000

#Number of hurdles
n = 10

#Probability of  clearing a hurdle
p = 5/6


#Theoretical probability of knocking down fewer than 2 hurdles
k = 1
print(binom.cdf(k, n, 1-p),3*(5/6)**10)


#Simulating the probability using  the binomial random variable
data_binom = binom.rvs(n,1-p,size=simlen) #Simulating the event of jumping 10 hurdles
err_ind = np.nonzero(data_binom <=k) #checking probability condition
err_n = np.size(err_ind) #computing the probability
print(err_n/simlen)
#print(data_binom)


#Simulating the probability using  the bernoulli random variable
data_bern_mat = bernoulli.rvs(1-p,size=(n,simlen))
data_binom=np.sum(data_bern_mat, axis=0)
#print(data_bern_mat)
#print(data_binom)
err_ind = np.nonzero(data_binom <=k) #checking probability condition
err_n = np.size(err_ind) #computing the probability
print(err_n/simlen)
