import numpy as np
import matplotlib.pyplot as plt
import xlrd
plt.rcdefaults()
#reding the table
loc=("/home/krishnajakodali/probstat/stat/tables/exer38/inp38.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
#initializing array to store data
section=[]
number=[]
for element in range(sheet.nrows-1):
	section.append("empty")
	number.append(0)
#excel data to arrays
for i in range(1,sheet.nrows):
	 section[i-1]=sheet.cell_value(i,0)
	 number[i-1]=sheet.cell_value(i,1)

#plotting bar graph
#index=np.arrange(len(cause))
index=[0,1,2,3,4,5,6]
plt.bar(section,number)
plt.xlabel('Sections of indian society',fontsize=5)
plt.ylabel('Number of girls per 1000 boys',fontsize=5)
plt.xticks(index,section,fontsize=5,rotation=15)
plt.title("Number of girls per 1000 boys in different sections of indian society")
plt.savefig('./pyfigs/exer38.eps')



plt.show()


