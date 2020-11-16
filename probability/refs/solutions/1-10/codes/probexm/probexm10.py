import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd

loc = ("../../table/probexm/probexm10.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

f1=0
f2= 0
f3= 0

fx = 5
count = 0
for j in range(1, 6):
	if sheet.cell_value(j, 1) > 40:
		count = count+1

f1 = count
count= 0
		
for j in range(1, 6):
	if sheet.cell_value(j, 1)==49:
		count = count+1
		
f2 = count
count= 0
		
for j in range(1, 6):
	if sheet.cell_value(j, 1) >35:
		count = count+1
	
f3 = count
count= 0
	




p1 = f1/fx	
p2 = f2/fx	
p3 = f3/fx

	
print(fx)
print("P(X>40)={}".format(p1))
print("P(X=49)={}".format(p2))
print("P(X>35)={}".format(p3))


objects = ('X>40', 'X=49', 'X>35')
y_pos = np.arange(len(objects))
performance = [p1,p2,p3]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.savefig('../../figures/probexm/probexm10.eps')

plt.show()
