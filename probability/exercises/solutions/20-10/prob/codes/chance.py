import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
simlen=int(1e5)
sample_size=8
#pointing at 8
event_size1=1
prob1=event_size1/sample_size
#pointing at odd(1,3,5,7)
event_size2=4
prob2=event_size2/sample_size
#pointing at number greater than 2 (3,4,5,6,7,8)
event_size3=6
prob3=event_size3/sample_size
#pointing at number less than 9 (1,2,3,4,5,6,7,8)
event_size4=8
prob4=event_size4/sample_size
#Simulations using Bernoulli r.v.
data_bern1 = bernoulli.rvs(size=simlen,p=prob1)
data_bern2= bernoulli.rvs(size=simlen,p=prob2)
data_bern3 = bernoulli.rvs(size=simlen,p=prob3)
data_bern4 = bernoulli.rvs(size=simlen,p=prob4)



#Calculating the number of favourable outcomes
err_ind1 = np.nonzero(data_bern1 == 1)
err_ind2 = np.nonzero(data_bern2 == 1)
err_ind3 = np.nonzero(data_bern3 == 1)
err_ind4 = np.nonzero(data_bern4 == 1)
print(err_ind1)
print(err_ind2)
print(err_ind3)
print(err_ind4)

#calculating the probability
err_n1 = np.size(err_ind1)/simlen
err_n2 = np.size(err_ind2)/simlen
err_n3 = np.size(err_ind3)/simlen
err_n4 = np.size(err_ind4)/simlen


#Theory vs simulation
print(err_n1,prob1)
print(err_n2,prob2)
print(err_n3,prob3)
print(err_n4,prob4)
