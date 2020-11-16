import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
sample_size=144
event_size=20
prob=event_size/sample_size


data_bern = bernoulli.rvs(size=1000,p=prob)
# ax = sns.distplot(data_bern,
# 					bins=int(10),
# 	                 kde=True,	               
# 	                color='crimson',
#                   hist_kws={"linewidth": 25,'alpha':1})
# ax.set(xlabel='Bernouli', ylabel='P_Density')                 
# plt.show()
