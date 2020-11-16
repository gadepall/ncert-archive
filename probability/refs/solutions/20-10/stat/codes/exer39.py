import numpy as np
import matplotlib.pyplot as plt
import xlrd
plt.rcdefaults()
#reding the table
loc=("/home/krishnajakodali/probstat/stat/tables/exer39/inp39.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
#initializing array to store data
party=[]
seats=[]
for element in range(sheet.nrows-1):
	party.append('E')
	seats.append(0)
#excel data to arrays
for i in range(1,sheet.nrows):
	 party[i-1]=sheet.cell_value(i,0)
	 seats[i-1]=sheet.cell_value(i,1)

#plotting bar graph
#index=np.arrange(len(cause))
index=[0,1,2,3,4,5]
plt.bar(party,seats)
plt.xlabel('Political parties',fontsize=7)
plt.ylabel('Number of seats won',fontsize=7)
plt.xticks(index,party,fontsize=10,rotation=0)
plt.title("Seats won by varius political parties")
plt.savefig('./pyfigs/exer39.eps')



plt.show()
#max seats
greatest=max(seats)
for i in range(len(seats)):
	if seats[i]==greatest:
		print(party[i])

