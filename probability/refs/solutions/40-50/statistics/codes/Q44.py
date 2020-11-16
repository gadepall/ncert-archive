import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_excel('tables/Q44/prob.xlsx',index_col= None)
x_pos= [1.5,2.5,4,6,8.5,12.5,16]
freq=data['No.of children'].values.tolist()

width = [1,1,2,2,3,5,2] #Making aspect ratio of bar graph similar to histogram
plt.bar(x_pos, freq, width=width)
plt.xlabel('Age (in years)')
plt.ylabel('No.of children')
plt.xlim(0,19)
plt.xticks(range(0,19,1))
plt.yticks(range(0,14,1))
plt.grid()
plt.show()
