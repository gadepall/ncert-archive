import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
data_binom = binom.rvs(n=3,p=0.5,size=1000)
ax = sns.distplot(data_binom,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})
print(np.count_nonzero(data_binom==0))
plt.show()
