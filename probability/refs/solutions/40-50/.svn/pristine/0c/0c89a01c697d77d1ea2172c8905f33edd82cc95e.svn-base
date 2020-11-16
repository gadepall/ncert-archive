import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from functions import *


#Calculating probability using bernoulli simulation


#Probability that A solves
p_1= bernoulli_success_prob(0.5)
#Probability that B solves
p_2= bernoulli_success_prob(1/3)

#Probability that question is solved
prob= p_1*p_2 + p_1*(1-p_2) + (1-p_1)*p_2
print(prob)

#Probability that exactly one of them solves the question
prob= p_1*(1-p_2) + (1-p_1)*p_2
print(prob)
