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

#operations of signal
# x=np.array([float(i) for i in input("Enter the A=Sequence:" ).split(",")])
# t0=float(input("Enter the Shifting Factor: "))
# A=float(input("Enter the Scale Factor: "))
# t= np.linspace(min(0,t0-1),max(t0+1,len(x)),len(x))
# plt.plot(t,x)
# plt.plot(-t,x)
# plt.plot(t+t0,x)
# plt.plot(t,A*x)
# plt.plot(t0+t,A*x)
# plt.show()

#Toeplitz Method

x=np.array(input("Enter the Sequence x:").split(",")).astype(int)

h=np.array(input("Enter the Sequence h:").split(",")).astype(int)
hn=h
row = len(x)
column=len(x)+len(h)-1

if(len(h)<column):
    z=np.zeros(column-len(h))
    h=np.concatenate((h,z))
toeplitz= h
for i in range(row-1):
    h=np.roll(h,1)
    toeplitz=np.concatenate((toeplitz,h))
toeplitz.shape=(row,column)
toeplitz= np.transpose(toeplitz)
print(np.dot(toeplitz,x).astype(int))
print(np.convolve(x,hn))        