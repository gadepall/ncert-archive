import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
simlen=int(1e5)
sample_size=52
#drawing a king of red
event_size1=2
prob1=event_size1/sample_size
#face card
event_size2=12
prob2=event_size2/sample_size
#red face card
event_size3=6
prob3=event_size3/sample_size
#jack of hearts
event_size4=1
prob4=event_size4/sample_size
#spade
event_size5=13
prob5=event_size5/sample_size
#queen od diamonds
event_size6=1
prob6=event_size6/sample_size
#Simulations using Bernoulli r.v.
data_bern1 = bernoulli.rvs(size=simlen,p=prob1)
data_bern2= bernoulli.rvs(size=simlen,p=prob2)
data_bern3 = bernoulli.rvs(size=simlen,p=prob3)
data_bern4 = bernoulli.rvs(size=simlen,p=prob4)
data_bern5 = bernoulli.rvs(size=simlen,p=prob5)
data_bern6 = bernoulli.rvs(size=simlen,p=prob6)



#Calculating the number of favourable outcomes
err_ind1 = np.nonzero(data_bern1 == 1)
err_ind2 = np.nonzero(data_bern2 == 1)
err_ind3 = np.nonzero(data_bern3 == 1)
err_ind4 = np.nonzero(data_bern4 == 1)
err_ind5 = np.nonzero(data_bern5 == 1)
err_ind6 = np.nonzero(data_bern6 == 1)
#calculating the probability
err_n1 = np.size(err_ind1)/simlen
err_n2 = np.size(err_ind2)/simlen
err_n3 = np.size(err_ind3)/simlen
err_n4 = np.size(err_ind4)/simlen
err_n5 = np.size(err_ind5)/simlen
err_n6 = np.size(err_ind6)/simlen


#Theory vs simulation
print(err_n1,prob1)
print(err_n2,prob2)
print(err_n3,prob3)
print(err_n4,prob4)
print(err_n5,prob5)
print(err_n6,prob6)
