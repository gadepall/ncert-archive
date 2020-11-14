import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
import xlrd

loc = ("../../table/prob/prob9.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

sample_size=30
s = 0
for i in range(1,19):
	a = sheet.cell_value(i, 0 )
	if(a>=0.12 and a<=0.16):
		s = s+sheet.cell_value(i, 1 )
		
event_size=s
prob=event_size/sample_size
#Simulations using Bernoulli r.v.
data_bern = bernoulli.rvs(size=sample_size,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/sample_size

#Theory vs simulation
print(err_n,prob)
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(4.5,3)})
ax= sns.distplot(data_bern,
                 kde=False,
                 color="skyblue",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Bernoulli', ylabel='Frequency')
plt.savefig('../../figures/prob/prob10.eps')
plt.show()
