import numpy as np
import matplotlib.pyplot as plt
import xlrd
import xlsxwriter
#reding the table
loc=("/home/krishnajakodali/probstat/stat/tables/exer32/sulphur.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
#outpul excel table
workbook=xlsxwriter.Workbook('/home/krishnajakodali/probstat/stat/tables/exer32/out32.xlsx')
worksheet=workbook.add_worksheet()
cell_format=workbook.add_format()
cell_format.set_border()
#grouped frequency distribution table specifications
class_width=0.04
start_value=0.00
end_value=0.24
#number of classes
total_classes=int((end_value-start_value)/class_width)

#initializing array to store class frequency
freq=[]
for element in range(total_classes):
	freq.append(0)
#Grouping data
for i in range(sheet.nrows):
	for j in range(sheet.ncols):
		for n in range(total_classes):
			if sheet.cell_value(i,j)<((n+1)*class_width+start_value) and sheet.cell_value(i,j)>=((n)*class_width+start_value):
				freq[n]=freq[n]+1

#creating frequency distribution table
worksheet.write(0,0,"Class",cell_format)
worksheet.write(0,1,"Class frequency",cell_format)
for k in range(total_classes):
	worksheet.write(k+1,0,str((class_width*k)+start_value)+'-'+str((class_width*(k+1))+start_value),cell_format)
	worksheet.write(k+1,1,freq[k],cell_format)
workbook.close()
#no of days with conc more than 0.11 ppm
days=0
for i in range(sheet.nrows):
	for j in range(sheet.ncols):
		if sheet.cell_value(i,j)>0.11:
			days=days+1
print(days)
