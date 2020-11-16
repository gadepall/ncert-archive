import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd

loc = ("../../table/prob/prob1.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)


fx = 0
for j in range(1, sheet.nrows):
	fx = fx + sheet.cell_value(j, 1)
	
	
f1= sheet.cell_value(1, 1)
f2= sheet.cell_value(2, 1)
f3= sheet.cell_value(3, 1)

p1 = f1/fx	
p2 = f2/fx	
p3 = f3/fx	
print(fx)
print("P(X=2)={}".format(p1))
print("P(X=1)={}".format(p2))
print("P(X=0)={}".format(p3))

objects = ('2 girls', '1 girl', 'no girl')
y_pos = np.arange(len(objects))
performance = [0.316,0.5427,0.1407]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.savefig('../../figures/prob/prob2.eps')

plt.show()
