import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd

loc = ("../../table/probexm/probexm6.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)


fx = 0
for j in range(1, sheet.nrows):
	fx = fx + sheet.cell_value(j, 1)
	
	
f1= sheet.cell_value(1, 1)
f2= 0
f3= 0

for j in range(3, 5):
	f2 = f2+ sheet.cell_value(j, 1)
	
for j in range(1, 4):
	f3 = f3 + sheet.cell_value(j, 1)
	

p1 = f1/fx	
p2 = f2/fx	
p3 = f3/fx

	
print(fx)
print("P(X<4K)={}".format(p1))
print("P(4K<X<14K)={}".format(p2))
print("P(X>9K)={}".format(p3))


objects = ('<4000', '>9000', '4000-14000')
y_pos = np.arange(len(objects))
performance = [0.179,0.15,0.157]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.savefig('../../figures/probexm/probexm6.eps')

plt.show()
