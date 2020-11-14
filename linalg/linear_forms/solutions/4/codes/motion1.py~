# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
# Create the vectors X and Y
x = np.linspace(0,15,300)
y =490 - 2.17*x ** 2  

# Create the plot
plt.plot(x,y,label='motion')

# Add a title
plt.title('')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')

# Add a Legend
plt.legend()
plt.savefig('../figures/motion.eps')
# Show the plot
plt.show()
