import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_excel('tables/Q45/prob.xlsx',index_col= None)
x_pos= [2.5,5,7,10,16]
freq=data['No.of surnames'].values.tolist()

width =[3,2,2,4,8] #Making aspect ratio of bar graph similar to histogram
plt.bar(x_pos, freq, width=width)
plt.xlabel('No.of letters')
plt.ylabel('No.of surnames')
plt.xlim(0,21)
plt.xticks(range(0, 21))
plt.yticks(range(0,45,4))
plt.grid()
plt.show()
