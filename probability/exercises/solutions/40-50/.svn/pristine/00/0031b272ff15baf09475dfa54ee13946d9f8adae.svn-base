import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_excel('tables/Q43/prob.xlsx',index_col= None)
x_pos= np.arange(-3.5,63.5,6.0) 
runsA=data['Team A'].values.tolist()
runsA.insert(0,0)
runsA.append(0)
runsB=data['Team B'].values.tolist()
runsB.insert(0,0)
runsB.append(0)
plt.plot(x_pos, runsA, color='g',label='Team A')
plt.plot(x_pos, runsB, color='r',label='Team B')
plt.xlabel('No.of balls')
plt.ylabel('Runs scored')
plt.xlim(-6,70)
plt.ylim(0,12)
plt.xticks(np.arange(-5.5,69.5,6))
plt.yticks(range(0,12))
plt.legend(loc='upper right')
plt.grid()
plt.show()
