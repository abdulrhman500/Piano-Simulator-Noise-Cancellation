import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import random
from scipy.fftpack import fft
import math
import array

def u(t):  # unit step function
    return 1*(t > 0)

pi = np.pi
end_time = 3          # end_of_time_input
sample = 12*1024      # the number of input samples
N = 6    # Number of frequancies
# array of 12*1024 number between 0 and 3 reprsenting time
t = np.linspace(0, end_time, sample)
f = [0, 0, 0, 0, 0, 0]  # Frequancy of 3rd octave notes
F = [392, 261.63, 392, 261.63, 392, 261.63]  # Frequancy of 4rd octave notes

ti = [0, 0.5, 1.1, 1.7, 2.3, 2.8]  # starting time of each frequancy

Ti = [0.4]*6  # duration of each frequancy

x = 0  # function of the  signal
for i in range(N):  # calculate the signal X for each time input t
    x += (np.sin(2*np.pi*f[i]*t)+np.sin(2*np.pi*F[i]*t)
          ) * (u(t-ti[i])-u(t-ti[i]-Ti[i]))

n = 3*1024
x_f=fft(x)    ##signal in frequancy domain
x_f = 2/n * np.abs(x_f[0:np.int(n/2)])

ff = np. linspace(0 , 512 , int(n/2))  ##frequancy domain

fn1,fn2 = np.random.randint(0,512,2)   ##the 2 random noise frequancy
𝑛oise = np.sin(2*𝑓𝑛1*pi*𝑡) + np.sin(2*𝑓𝑛2*pi*t)  ## the noise
x_noised=x+noise    ##the orignal signal + the noise
# sd.play(x, end_time*1024)
x_f_noised = fft(x_noised)
x_f_noised = 2/n * np.abs(x_f_noised[0:np.int(n/2)])

values=np.where(x_f_noised>math.ceil(np.max(x_f))) ## indicies of frequancies in the noiesd signal > the max frequancy in  the original signal 

##  the frequancies of the noise
i1=int(ff[values[0][0]])
i2=int(ff[values[0][1]])


x_filtered=x_noised-(np.sin(2*i1*pi*𝑡) + np.sin(2*i2*pi*t))## the signal after removing the noise
x_filtered_f=fft(x_filtered)
x_filtered_f=2/n * np.abs(x_filtered_f[0:np.int(n/2)])

####################################################################
##Printing plots

plt.subplot(3,2,1)
plt.plot(t,x)
plt.title("X(t)")

plt.subplot(3,2,2)
plt.plot(ff,x_f)
plt.title("X(f)")

plt.subplot(3,2,3)
plt.plot(t,x_noised)
plt.title("Xn(t)")

plt.subplot(3,2,4)
plt.plot(ff, 2/N * np.abs(fft(x_noised) [0:np.int(n/2)]))
plt.title("Xn(f)")


plt.subplot(3,2 ,5)
plt.plot(t,x_filtered)
plt.title("X_filtered(t)")

plt.subplot(3,2 ,6)
plt.plot(ff,x_filtered_f)
plt.title("X_filtered(f)")

sd.play(x_filtered, 3*1024)

#######################
# 174.61  F3
# 130.81  c3
# 146.83  D3
# 261.63  c4
# 293.66  D4
# 392     G4
# x+=np.where(np.logical_and(t>=ti[i],t<=ti[i]+Ti[i]),(np.sin(2*np.pi*f[i]*t)+np.sin(2*np.pi*F[i]*t)),0)
