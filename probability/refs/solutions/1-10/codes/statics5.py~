import xlrd

loc = ("../table/table522.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

f=0
fx = 0
for i in range(1, sheet.nrows):
	f= f + sheet.cell_value(i, 1)
	
for j in range(1, sheet.nrows):
	fx = fx + sheet.cell_value(j, 3)

print(f)
print(fx)
#fx = table[0][3] +table[1][3] +table[2][3] +table[3][3] +table[4][3]
m = fx/f
print("Mean ={}".format(m))
