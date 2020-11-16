import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd

loc = ("../../table/probexm/probexm8.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)


fx = 2000

	
	
f1= sheet.cell_value(2, 4)
f2= 0
f3= 0

for j in range(2, 5):
	f2 = f2+ sheet.cell_value(3, j)
	
for j in range(2, 5):
	f3 = f3 + sheet.cell_value(j, 1)
	

p1 = f1/fx	
p2 = f2/fx	
p3 = f3/fx

	
print(fx)
print("P(X=1)={}".format(p1))
print("P(X=2)={}".format(p2))
print("P(X=3)={}".format(p3))


objects = ('X=1', 'X=2', 'X=3')
y_pos = np.arange(len(objects))
performance = [p1,p2,p3]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.savefig('../../figures/probexm/probexm8.eps')

plt.show()
