import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli


def bayes_theorem(p_e1,p_e2,p_xgiven_e1,p_xgiven_e2):
	p_x= p_e1*p_xgiven_e1 + p_e2*p_xgiven_e2
	numerator1 = p_e1*p_xgiven_e1
	p_e1given_x=numerator1/p_x
	return p_e1given_x
	

def bernoulli_success_prob(success):
	simlen=int(1e5)
	data_bern = bernoulli.rvs(size=simlen,p=success)
	#print(data_bern)
	#Calculating the number of favourable outcomes
	err_ind = np.nonzero(data_bern == 1)
	#calculating the probability
	err_n = np.size(err_ind)/simlen
	return err_n
	
def total_prob(p_e1,p_e2,p_xgiven_e1,p_xgiven_e2):
	p_x= p_e1*p_xgiven_e1 + p_e2*p_xgiven_e2
	return p_x
