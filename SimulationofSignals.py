import numpy as np
import matplotlib.pyplot as plt


# unit impulse Signal
x=np.arange(-10,10,0.01)
y=np.zeros(len(x))
y[np.isclose(x,0,atol=0.00000001)]=1
plt.plot(x,y,'g')
plt.show()

