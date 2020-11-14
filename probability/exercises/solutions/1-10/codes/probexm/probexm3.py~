import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd

loc = ("../../table/probexm/probexm3.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)


fx = 0
for j in range(1, sheet.nrows):
	fx = fx + sheet.cell_value(j, 1)
	
	
f1= sheet.cell_value(1, 1)
f2= sheet.cell_value(2, 1)
f3= sheet.cell_value(3, 1)
f4= sheet.cell_value(4, 1)
f5= sheet.cell_value(5, 1)
f6= sheet.cell_value(6, 1)

p1 = f1/fx	
p2 = f2/fx	
p3 = f3/fx
p4 = f4/fx	
p5= f5/fx	
p6 = f6/fx	
	
print(fx)
print("P(X=1)={}".format(p1))
print("P(X=2)={}".format(p2))
print("P(X=3)={}".format(p3))
print("P(X=4)={}".format(p4))
print("P(X=5)={}".format(p5))
print("P(X=6)={}".format(p6))

objects = ('1', '2', '3','4','5','6')
y_pos = np.arange(len(objects))
performance = [0.179,0.15,0.157,0.149,0.175,0.19]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.savefig('../../figures/probexm/probexm3.eps')

plt.show()
