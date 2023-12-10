import numpy as np
import matplotlib.pyplot as plt 
import cmath


#using maths eqaution
# x=np.array(input("Enter the sequence").split(",")).astype(int)
# k=len(x)
# k_array=np.arange(0,k,1)
# y=np.zeros(k,dtype=complex)
# for i in range(k):
#     sum=0
#     for m in range(k):
#         sum+=x[m]*np.exp(complex((-1j)*2*np.pi*i*m*float(1/k)))
#     y[i]=sum   
# print("Dft  is :",y)
# mag_y = [np.abs(k) for k in y]
# plt.stem(k_array,mag_y)
# plt.show()
# phase_y=[cmath.phase(k) for k in y]
# plt.stem(k_array,phase_y)
# plt.show()   

#N point dft 
# x=np.array(input("Enter the sequence: ").split(",")).astype(int)
# xn=x
# N=int(input("Enter the N point: "))

# if (N!=len(x)):
#     if(N>len(x)):
#         z=np.zeros(N-len(x))
#         x=np.concatenate((x,z))
         
# def dft(x):
#     k=len(x)
#     k_array=np.arange(0,k,1)
#     y=np.zeros(k,dtype=complex)
#     for i in range(k):
#         sum=0
#         for m in range(k):
#          sum+=x[m]*np.exp(complex((-1j)*2*np.pi*i*m*float(1/k)))
#         y[i]=sum   
#     return y
# mn=dft(x)

    
# print("Dft  is :",mn)
# k=len(x)
# kn_array = np.arange(0,k,1)
# mag_y = [np.abs(k) for k in mn]
# plt.stem(kn_array,mag_y)

# plt.show()
# phase_y=[cmath.phase(k) for k in mn]
# plt.stem(kn_array,phase_y)

# plt.show()

#dft using matrix
# x=np.array(input("Enter the sequence: ").split(",")).astype(int)
# xn=x
# k=len(x)
# k_array=np.arange(0,k,1)
# twiddle= np.ones(k,dtype=complex)

# for i in  range(1,k):
#     for j in range(k):
#         num = np.exp(complex((-1j)*2*np.pi*i*j*(1/k)))
#         twiddle = np.append(twiddle,num)
# twiddle.shape=(k,k)
# y=np.dot(twiddle,x)
# print("dft using matrix",y)        
# print(np.fft.fft(x))    

#circular convolution

# x1=np.array(input("Enter the sequence1: ").split(",")).astype(int)
# x2=np.array(input("Enter the sequence2: ").split(",")).astype(int)
# if len(x1)<len(x2):
#     x1= np.pad(x1,(0,len(x2-(x1))))
# elif len(x1)>len(x2):
#      x2= np.pad(x2,(0,len(x1-(x2))))


# k=len(x1)
# X1=np.fft.fft(x1)
# X2=np.fft.fft(x2)
# X=X1*X2
# print("lhs: ",np.fft.ifft(X).astype(int))
# z=x1
# for i in range(k-1):
#     x1=np.roll(x1,1)
#     z=np.concatenate((z,x1))
# z=z.reshape(k,k)
# z=np.transpose(z)
# rhs = np.dot(z,x2)
# print("rhs: ",rhs)    
    
    
#Parsevals theorem

def dft(x,k):
    y=np.zeros(k,dtype=complex)
    for i in range(k):
        sum=0 
        for m in range(k):
            sum+=x[m]*np.exp(complex((-1j)*2*np.pi*i*m*(1/k)))
        y[i]=sum
    return y

x=np.array(input("Enter the sequence:").split(",")).astype(int)
k=len(x)
p=dft(x,k)

lhs=float(sum(abs(x*x))) 
rhs=sum((abs(p*p))/k)
print("lhs",lhs)
print("Rhs",rhs)       