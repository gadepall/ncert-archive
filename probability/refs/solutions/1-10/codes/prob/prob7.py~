import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
import xlrd

loc = ("../../table/prob/prob10.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

sample_size = 40
event_size1 = 0
event_size2 = 0
event_size3 = 0
s=0
t=0



for i in range(1, 22):
	s = s + sheet.cell_value(i, 0)
	if(s<7):
		event_size1 = event_size1 + sheet.cell_value(i,1)
for j in range(1, 22):
	t = t + sheet.cell_value(j, 0)
	if(t>=7):
		event_size2 = event_size2 + sheet.cell_value(j,1)

prob1=event_size1/sample_size
prob2=event_size2/sample_size
prob3=event_size3/sample_size
print("P(X<7)={}".format(prob1))
print("P(X>=7)={}".format(prob2))
print("P(X<=1\2)={}".format(prob3))

print(sample_size)
objects = ('less than 7km', 'more than 7km','within 1/2 km')
y_pos = np.arange(len(objects))
performance = [prob1,prob2,prob3]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.savefig('../../figures/prob/prob7.eps')
plt.show()



