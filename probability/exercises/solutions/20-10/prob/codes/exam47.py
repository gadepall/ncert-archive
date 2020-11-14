import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
#probabilities
probC=0.8
probI=1-probC
probAC=(9/10)**2
probAI=(4/10)**2
#Simulations using Bernoulli r.v.
#simlen is made propotional to the probability of the machines 
simlen1=int(probC*(1e7))
simlen2=int(probI*(1e7))
print(simlen1)
#production of coorectly set up machines
data_bernC = bernoulli.rvs(size=simlen1,p=probAC)
#production of incorrectly setup machines
data_bernI= bernoulli.rvs(size=simlen2,p=probAI)


#Calculating the number of favourable outcomes
err_ind1 = np.nonzero(data_bernC == 1)
err_ind2 = np.nonzero(data_bernI == 1)
err_n1=np.size(err_ind1)
err_n2=np.size(err_ind2)

#calculating the probability that they come from a mchine correctly set up
probCA=err_n1/(err_n1+err_n2)

#theoritical probability using bayes thm
prob=probC*probAC/(probC*probAC+probI*probAI)

#Theory vs simulation
print(probCA,prob)
