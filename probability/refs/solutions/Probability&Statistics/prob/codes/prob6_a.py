import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
#There are four possible outcomes,
#{H,H}, {H,T}, {T,H}, {T,T}
sample_size=4
#All events are equally probable, so therefore
#Happening of an event is 
event_size=1
prob=event_size/sample_size
#Simulations using Bernoulli r.v.
data_bern = bernoulli.rvs(size=10,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/sample_size

#Theory vs simulation
print(err_n,prob)
