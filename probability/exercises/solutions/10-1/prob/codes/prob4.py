import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
sample_size=2**3
event_size=6
prob=event_size/sample_size
data_bern = bernoulli.rvs(size=1000,p=prob)
# ax = sns.distplot(data_bern,
# 	                 kde=True,
# 	                 hist=True,
# 	                 bins=int(10),
# 	                color='crimson',
#                   hist_kws={"linewidth": 20,'alpha':1})
# ax.set(xlabel='Bernouli', ylabel='Frequency')

# plt.show()
