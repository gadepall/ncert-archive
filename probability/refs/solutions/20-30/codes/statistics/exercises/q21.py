import xlrd
loc = ("../../../tables/statistics/exercises/stat_ex_q21_ans.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)
f=0
fx=0

for i in range(1,sheet.nrows):
	f = f + sheet.cell_value(i,1)

for j in range(1,sheet.nrows):
	fx = fx + sheet.cell_value(j,3)	
	
m = fx/f
print("Mean = {}".format(m))

print("-------------------------------------------------MOVING-----TO---MEDIAN----------------------")
import math
n = 0
n1 = 0
f = 0
s1 = 9999
fx = 0
a = 1
h = 3

for i in range(1,sheet.nrows):
	n = n + sheet.cell_value(i,1)
	
f1 = n/2
for i in range(1,sheet.nrows):
	s = math.fabs(sheet.cell_value(i,1) - (f1))
	if s1 > s:
		s1 = s
		n1 = i

cf = 0#sheet.cell_value(n1-1,1)
for i in range(1,n1):
	cf = cf + sheet.cell_value(i,1)
f = sheet.cell_value(n1,1)
l = a + (n1-1)*h
#l = 1 + (3-1)*3
me = l + ((f1 - cf)/(f))*h

print("cf={}".format(cf))
print("f1={}".format(f1))
print("n={}".format(n))
print("h={}".format(h))
print("l={}".format(l))
print("n1={}".format(n1))
print("median={}".format(me))

print("-------------------------------------------------MOVING-----TO---MODE----------------------")
f1=0
for i in range(1,sheet.nrows):
	n = n + sheet.cell_value(i,1)
	

for i in range(1,sheet.nrows):
	s = math.fabs(sheet.cell_value(i,1) - (n/2))
	if s1 > s:
		s1 = s
		n1 = i

cf = 0#sheet.cell_value(n1-1,1)
for i in range(1,n1):
	cf = cf + sheet.cell_value(i,1)
f0 = sheet.cell_value(n1-1,1)
f1 = sheet.cell_value(n1,1)
f2 = sheet.cell_value(n1+1,1)
l = a + (n1-1)*h
#l = 1 + (3-1)*3
mo = l + ((f1 - f0)/(2*f1 - f0 - f2))*h

print("cf={}".format(cf))
print("f1={}".format(f1))
print("n={}".format(n))
print("h={}".format(h))
print("l={}".format(l))
print("n1={}".format(n1))
print("mode={}".format(mo))

