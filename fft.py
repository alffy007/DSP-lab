import numpy as np
import matplotlib.pyplot as plt

def dit_fft(x):
    N=len(x)
    if N<=1:
        return x
    even=dit_fft(x[0::2])
    odd=dit_fft(x[1::2])
    T=[np.exp(-2j*np.pi*k/N)*odd[k] for k in range (N//2)]
    return [even[k]+T[k] for k in range (N//2)]+[even[k]-T[k]  for k in range (N//2)]

def dit_ifft(x):
    N=len(x)
    if N<=1:
        return x
    even=dit_ifft(x[0::2])
    odd=dit_ifft(x[1::2])
    T=[np.exp(2j*np.pi*k/N)*odd[k] for k in range (N//2)]
    return [(even[k]+T[k])/2 for k in range (N//2)]+[(even[k]-T[k])/2  for k in range (N//2)]

x=np.array(input("enter the sequence x: ").split(",")).astype(complex)
X_dit_fft =dit_fft(x)    
X_dit_ifft =dit_ifft(x)
print(X_dit_fft)
# print(X_dit_ifft) 
# print("fft fun",np.fft.fft(x))
 