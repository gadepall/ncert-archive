import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
simlen=int(1e5)
sample_size=3
#yellow ball
event_size1=1
prob1=event_size1/sample_size
#red ball
event_size2=1
prob2=event_size2/sample_size
#blue ball
event_size3=1
prob3=event_size3/sample_size
#Simulations using Bernoulli r.v.
data_bern1 = bernoulli.rvs(size=simlen,p=prob1)
data_bern2= bernoulli.rvs(size=simlen,p=prob2)
data_bern3 = bernoulli.rvs(size=simlen,p=prob3)



#Calculating the number of favourable outcomes
err_ind1 = np.nonzero(data_bern1 == 1)
err_ind2 = np.nonzero(data_bern2 == 1)
err_ind3 = np.nonzero(data_bern3 == 1)

#calculating the probability
err_n1 = np.size(err_ind1)/simlen
err_n2 = np.size(err_ind2)/simlen
err_n3 = np.size(err_ind3)/simlen


#Theory vs simulation
print(err_n1,prob1)
print(err_n2,prob2)
print(err_n3,prob3)
