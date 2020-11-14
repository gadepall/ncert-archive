import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


m = 100000
k = np.linspace(1,10,m)
p = (2**k-1)/(6**k-5**k)
print(p[-1])
plt.plot(k,p)

plt.savefig('test.pdf')
plt.savefig('test.eps')
subprocess.run(shlex.split("termux-open test.pdf"))
