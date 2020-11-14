import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
simlen = int(1e5)
sample_size=6
event_size=3.14/4
prob=event_size/sample_size
data_bern = bernoulli.rvs(size=simlen,p=prob)
#storing the index for the received symbol 
#in error
err_ind = np.nonzero(data_bern == 1)
#calculating the total number of errors
err_n = np.size(err_ind)/simlen

print(err_n,prob)
