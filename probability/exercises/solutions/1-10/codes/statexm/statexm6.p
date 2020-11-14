import xlrd

loc = ("../../table/statexm/statexm5.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)
n = 0
f1 = 0
f= 0
fx = 0

for i in range(1,sheet.nrows):
	f = f +  sheet.cell_value(i,2)
	
for i in range(1,sheet.nrows):
	fx = fx +  sheet.cell_value(i,3)	


for i in range(1, sheet.nrows):
	if f1 < sheet.cell_value(i,2):
		f1=sheet.cell_value(i,2)
		n= i

mean = fx/f

h =	sheet.cell_value(2,1) - sheet.cell_value(1,1)
l = (h - (h/2)) + (n-1)*h
f0 = sheet.cell_value(n-1,2)
f2 = sheet.cell_value(n+1,2)
m = l+ ((f1 - f0)/(2*f1 - f0 - f2))*h


print("f = {}".format(f))
print("Mean = {}".format(mean))

print("f1 = {}".format(f1))
print("n = {}".format(n))
print("h = {}".format(h))
print("l = {}".format(l))
print("f0 = {}".format(f0))
print("f2= {}".format(f2))
print("Median = {}".format(m))
