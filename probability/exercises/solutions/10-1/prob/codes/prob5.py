import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
sample_size=6
event_size1=25
event_size2=11
prob1=event_size1/sample_size
prob2=event_size2/sample_size
data_bern1 = bernoulli.rvs(size=1000,p=prob1)
data_bern2 = bernoulli.rvs(size=1000,p=prob2)
# ax = sns.distplot(data_bern,
# 	                 kde=True,
# 	                 hist=True,
# 	                 bins=int(10),
# 	                color='crimson',
#                   hist_kws={"linewidth": 20,'alpha':1})
# ax.set(xlabel='Bernouli', ylabel='Frequency')

# plt.show()
