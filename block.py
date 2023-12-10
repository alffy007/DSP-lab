import numpy as np
import matplotlib.pyplot as plt
def overlapAdd(x,h):
    L=len(x)+len(h)-1
    N_fft = 2**(int(np.ceil(np.log2(L))))
    X=np.fft.fft(np.pad(x,(0,(N_fft-len(x)))))
    H=np.fft.fft(np.pad(h,(0,(N_fft-len(h)))))
    Y=X*H
    Y=np.real(np.fft.ifft(Y))
    Y=Y[:L]
    return Y

def  overlapsave(x,h,N):
    M=len(h)
    L=N-M+1
    x_pad=np.concatenate((x,np.zeros(N-1)))
    h_pad=np.concatenate((h,np.zeros(N-M)))
    y=np.zeros(len(x)+M-1)
    for i in range(0,len(x),L):
        x_segment=x_pad[i:i+N]
        
        X=np.fft.fft(x_segment)
        H=np.fft.fft(h_pad,N)
        Y=X*H
        Y_segment=np.fft.ifft(Y)
    
        Y=np.real(Y_segment)

    return Y


x=np.array(input("enter the sequence x: ").split(",")).astype(int)
h=np.array(input("enter the sequence h: ").split(",")).astype(int)
N=len(x)+len(h)-1
res=overlapsave(x,h,N)
print(res)
print(np.convolve(x,h))
