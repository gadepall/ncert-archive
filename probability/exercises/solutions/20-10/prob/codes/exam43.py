import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import xlrd
#reding the table
loc=("/home/krishnajakodali/probstat/prob/tables/boxes.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
#calculating probabilities from tables
prob=[0,0,0,0]
for i in range(1,sheet.nrows):
	total=0
	for j in range(1,sheet.ncols):
		total=total+sheet.cell_value(i,j)
	prob[i-1]=sheet.cell_value(i,1)/total
#total number of experiments
simlen=int(1e5)
#Simulations using Bernoulli r.v.
data_bern1 = bernoulli.rvs(size=simlen,p=prob[0])
data_bern2= bernoulli.rvs(size=simlen,p=prob[1])
data_bern3 = bernoulli.rvs(size=simlen,p=prob[2])
data_bern4 = bernoulli.rvs(size=simlen,p=prob[3])



#Calculating the number of favourable outcomes
err_ind1 = np.nonzero(data_bern1 == 1)
err_ind2 = np.nonzero(data_bern2 == 1)
err_ind3 = np.nonzero(data_bern3 == 1)
err_ind4 = np.nonzero(data_bern4 == 1)


#calculating the probability
err_n1 = np.size(err_ind1)/simlen
err_n2 = np.size(err_ind2)/simlen
err_n3 = np.size(err_ind3)/simlen
err_n4 = np.size(err_ind4)/simlen
#experimental conditional probability
err=err_n3/(err_n1+err_n2+err_n3+err_n4)
#theoritical probability using bayes thm
#all boxes are equiprobable
fprob=prob[2]/(prob[1]+prob[2]+prob[3]+prob[0])

#Theory vs simulation
print(err,fprob)
