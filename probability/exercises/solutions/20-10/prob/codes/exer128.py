import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
simlen=int(1e5)
sample_size=20
event_size=4
prob=event_size/sample_size
prob2=(sample_size-event_size-1)/(sample_size-1)
#Simulations using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
data_bern2 = bernoulli.rvs(size=simlen,p=prob2)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
err_ind2 = np.nonzero(data_bern2 == 1)
#calculating the probability
err_n = np.size(err_ind)/simlen
err_n2 = np.size(err_ind2)/simlen

#Theory vs simulation
print(err_n,prob)
print(err_n2,prob2)
