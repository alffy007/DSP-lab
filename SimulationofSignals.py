import numpy as np
import matplotlib.pyplot as plt


# unit impulse Signal

# x=np.arange(-10,10,0.01)
# y=np.zeros(len(x))
# y[np.isclose(x,0,atol=0.00000001)]=1
# plt.plot(x,y,'g')
# plt.show()

#Rectangular pulse ct

# x=np.arange(-10,10,0.01)
# w=int(input("Enter the width of Rectangular pulse: ")) 
# y=np.zeros(len(x))
# y[np.all([(x>=-w/2),(x<=w/2)],axis=0)]=1
# plt.plot(x,y,'r')
# plt.show()
# dt
# x=np.arange(-10,10)
# w=int(input("Enter the width of Rectangular pulse: ")) 
# y=np.zeros_like(x)
# y[(x>=-w/2) & (x<=w/2)]=1
# plt.stem(x,y,'r')
# plt.xticks(x)
# plt.show()

# Ramp Signal CT
# x=np.arange(-10,10,0.01)
# y=np.copy(x)
# y[y<0]=0
# plt.plot(x,y),
# plt.show()
# DT
# x=np.arange(-5,6)
# y=np.copy(x)
# y[y<0]=0
# plt.stem(x,y)
# plt.xticks(x)
# plt.show()


# Bipolar Pulse Signal CT
# x=np.arange(-10,10,0.01)
# y=np.zeros(len(x))
# y[np.all([(x>=-3)&(x<=0)],axis=0)]=-1
# y[np.all([(x>=0)&(x<=3)],axis=0)]=1
# plt.plot(x,y,'r')
# plt.show()
# DT
# x=np.arange(-10,10)
# y=np.zeros(len(x))
# y[np.all([(x>=-3)&(x<=0)],axis=0)]=-1
# y[np.all([(x>=0)&(x<=3)],axis=0)]=1
# plt.stem(x,y,'r')
# plt.xticks(x)
# plt.show()

# Triangular Signal CT
# x=np.arange(6)
# y=np.arange(4,-1,-1)
# z=np.concatenate([x,y])
# plt.plot(z)
# plt.show()
# DT
# x=np.arange(6)
# y=np.arange(4,-1,-1)
# z=np.concatenate([x,y])
# plt.stem(z)
# plt.xticks(np.arange(11))
# plt.show()


