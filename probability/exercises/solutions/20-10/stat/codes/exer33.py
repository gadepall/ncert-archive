import numpy as np
import matplotlib.pyplot as plt
import xlrd
import xlsxwriter
#reding the table
loc=("/home/krishnajakodali/probstat/stat/tables/exer33/heads33.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
#outpul excel table
workbook=xlsxwriter.Workbook('/home/krishnajakodali/probstat/stat/tables/exer33/out33.xlsx')
worksheet=workbook.add_worksheet()
cell_format=workbook.add_format()
cell_format.set_border()
#possible values are 0,1,2,3
total=4
#initializing array to store class frequency
freq=[]
for element in range(total):
	freq.append(0)
#Grouping data
for i in range(sheet.nrows):
	for j in range(sheet.ncols):
		for n in range(total):
			if sheet.cell_value(i,j)==n:
				freq[n]=freq[n]+1
tfreq=0
for f in freq:
	tfreq=tfreq+f
#creating frequency distribution table
worksheet.write(0,0,"no of heads",cell_format)
worksheet.write(0,1,"Frequency",cell_format)
for k in range(total):
	worksheet.write(k+1,0,k,cell_format)
	worksheet.write(k+1,1,freq[k],cell_format)
worksheet.write(total+1,0,"Total",cell_format)
worksheet.write(total+1,1,tfreq,cell_format)


workbook.close()
