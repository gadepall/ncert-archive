from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data_binom = binom.rvs(n=3,p=0.5,size=200)
ax = sns.distplot(data_binom,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')
plt.savefig('../../figures/prob/prob4.eps')
plt.show()
