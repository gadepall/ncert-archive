import numpy as np
import matplotlib.pyplot as plt

def print_value(x) :
  #slope of the line @ origin
    m_origin = x[1]/x[0]
  #slope of the required line
    m_line = -1/m_origin
  #required constant of the line
    c_line = x[1]-m_line*x[0]
  #presenting the value of slope and constant
    print("the slope of the m_line is ",m_line)
    print("the value of c in the line ",c_line) 
    x = np.linspace(-10,10,50)
    y= m_line*x+c_line
    plt.plot(x,y,'r',label="$L_{1}$")
    y1= m_origin*x
    plt.plot(x,y1,'b',label="$L_{2}$")
    plt.xlabel('Horizontal Axis')
    plt.ylabel('Vertical Axis')
    plt.legend()
    plt.grid()
    plt.xlim(-6,6)
    plt.ylim(-6,6)
    plt.plot(-1,2,'ro')
    plt.text(-3.5,2,'Intersection')
    plt.xticks(np.arange(-6, 6, step=1))
    plt.yticks(np.arange(-6, 6, step=1))
    plt.plot(x,[0]*50,'k')
    y=np.linspace(-10,10,50)
    plt.plot([0]*50,y,'k')
    plt.show()




z=[-1,2]
print_value(z)