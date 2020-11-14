import numpy as np
import matplotlib.pyplot as plt
import xlrd
import subprocess
import shlex
#reding the table
loc=("/home/krishnajakodali/probstat/stat/tables/exer37/femalefatality.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
#initializing array to store data
cause=[]
fatality=[]
for element in range(sheet.nrows-1):
	cause.append("empty")
	fatality.append(0)
#excel data to arrays
for i in range(1,sheet.nrows):
	 cause[i-1]=sheet.cell_value(i,0)
	 fatality[i-1]=sheet.cell_value(i,1)

#plotting bar graph
#index=np.arrange(len(cause))
index=[0,1,2,3,4,5]
plt.bar(index,fatality)
plt.xlabel('Illnesses',fontsize=5)
plt.ylabel('Fatality rate',fontsize=5)
plt.xticks(index,cause,fontsize=5,rotation=15)
plt.title("Female fatality rate due to different illnesses")
plt.savefig('./pyfigs/exer37.eps')
plt.show()

#most and least freq
max_fatality=max(fatality)
for x in range(len(fatality)):
	if fatality[x]==max_fatality:
		print(cause[x])

