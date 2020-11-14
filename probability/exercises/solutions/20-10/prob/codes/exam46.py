import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
simlen=int(1e5)
sample_size=6
#getting a six
event_size=1
prob1=event_size/sample_size
#not getting a six
event_size2=5
prob2=event_size2/sample_size
#Simulations using Bernoulli r.v.
#results of A and B throwing a dice
data_bernA = bernoulli.rvs(size=simlen,p=prob1)
data_bernB= bernoulli.rvs(size=simlen,p=prob1)
#to calculate experimental probability
#a contains total number of times A can get a 6 first
a=0
b=0
for i in range(simlen):
	if(data_bernA[i]==1):
		a=a+1
	elif(data_bernB[i]==1):
		b=b+1
#calculation of probability using infinite gp formulae
A=prob1*(1/(1-prob2**2))
B=prob1*prob2*(1/(1-prob2**2))


#prob of A  winning
print(a/(a+b),A)
#prob of B  winning
print(b/(a+b),B)


