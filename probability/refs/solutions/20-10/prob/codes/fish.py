import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
simlen=int(1e5)
print(simlen)
sample_size=13
event_size=5
prob=event_size/sample_size
#Simulations using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
print(data_bern)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
print(err_ind)
#calculating the probability
err_n = np.size(err_ind)/simlen

#Theory vs simulation
print(err_n,prob)
