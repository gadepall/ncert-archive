import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_excel('tables/Q41/prob.xlsx',index_col= None)
x_pos= range(350,1050,100) 
lamps=data['Number of lamps'].values.tolist()
#plt.hist(lamps,bins=bin_edges)
width =100.0 #Making aspect ratio of bar graph similar to histogram
plt.bar(x_pos, lamps, width)
plt.xlabel('Lifetime of lamps(in hrs)')
plt.ylabel('Number of lamps')
plt.xlim(200,1100)
plt.yticks(range(0,92,4))
plt.grid()
plt.show()
