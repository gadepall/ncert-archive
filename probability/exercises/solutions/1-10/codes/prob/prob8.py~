import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
import xlrd

loc = ("../../table/prob/table82.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)
sample_size = 0

for i in range(2,7):
	for j in range(1,5):
		sample_size = sample_size + sheet.cell_value(i,j)


event_size1 = sheet.cell_value(4,3)
event_size2 = sheet.cell_value(6,2)
event_size3 = sheet.cell_value(2,1)
event_size4 = sheet.cell_value(2,3)
event_size5 = 0

for i in range(2,7):
	event_size5 = event_size4 + sheet.cell_value(i,2)
	
p1 = event_size1/sample_size
p2 = event_size2/sample_size
p3 = event_size3/sample_size
p4 = event_size4/sample_size
p5 = event_size5/sample_size


print("P(X=1)={}".format(p1))
print("P(X=2)={}".format(p2))
print("P(X=3)={}".format(p3))
print("P(X=4)={}".format(p4))
print("P(X=5)={}".format(p5))

	
objects = ('X=1', 'X=2','X=3','X=4','X=5')
y_pos = np.arange(len(objects))
performance = [p1,p2,p3,p4,p5]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.savefig('../../figures/prob/prob8.eps')
plt.show()
