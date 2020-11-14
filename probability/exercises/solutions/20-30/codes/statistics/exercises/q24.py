import xlrd
import math
loc = ("../../../tables/statistics/exercises/stat_ex_q24_ans.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)
n = 0
n1 = 0
f = 0
s1 = 9999
fx = 0
a = 38
h = 2

for i in range(1,sheet.nrows):
	n = n + sheet.cell_value(i,1)
	
f1 = n/2
for i in range(1,sheet.nrows):
	s = math.fabs(sheet.cell_value(i,1) - (f1))
	if s1 > s:
		s1 = s
		n1 = i

cf = sheet.cell_value(n1-1,2)
#for i in range(1,n1):
#	cf = cf + sheet.cell_value(i,1)
f = sheet.cell_value(n1,1)
l = a + (n1-2)*h
#l = 1 + (3-1)*3
m = l + ((f1 - cf)/(f))*h

print("cf={}".format(cf))
print("f1={}".format(f1))
print("f={}".format(f))
print("n={}".format(n))
print("h={}".format(h))
print("l={}".format(l))
print("n1={}".format(n1))
print("median={}".format(m))

