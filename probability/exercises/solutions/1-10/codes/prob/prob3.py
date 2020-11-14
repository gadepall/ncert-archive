import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt



objects = ('Jan', 'feb', 'mar','apr','may','jun','jul','aug','sep','oct','Nov','Dec')
y_pos = np.arange(len(objects))
performance = [3,4,2,2,5,1,2,6,3,4,4,4]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('No of student')
plt.savefig('../../figures/prob/prob3.eps')

plt.show()
