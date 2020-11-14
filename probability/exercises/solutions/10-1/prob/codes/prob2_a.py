import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
sample_size=144
event_size=124
prob=event_size/sample_size
#Simulations using Bernoulli r.v.
data_bern = bernoulli.rvs(size=sample_size,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/sample_size

#Theory vs simulation
print(err_n,prob)
