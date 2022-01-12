#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:14:16 2020

@author: guycarrault & ThomasLesaulnier
"""
#from matplotlib.pyplot import *
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
#from pylab import *
plt.close("all")




#calcul de la reponse impulsionnelle selon la methode de  Fourier
fe=44000
#pour selectionner 1661
fc1=1600
fc2=1700
b2,a2 = scipy.signal.iirfilter(N=2,Wn=[fc1*2/fe,fc2*2/fe],btype="bandpass",ftype="butter")
w,Hf=scipy.signal.freqz(b2,a2)
freq=w/(2*np.pi)
plt.figure()
plt.subplot(211)
plt.plot(freq,20*np.log10(np.absolute(Hf)))
plt.xlabel("freqence f/fe")
plt.ylabel("Gain G en dB")
plt.grid()
plt.subplot(212)
plt.plot(freq,np.unwrap(np.angle(Hf)))
plt.xlabel("frequence f/fe")
plt.ylabel("phase en radians")
plt.grid()




#simulation d une sinusoïde   
plt.figure(6)
fe=44000
f1=1660
fo=1000
duree=1

##########
import math
import numpy as np
from matplotlib.pyplot import *
import scipy.io.wavfile as wave
from numpy.fft import fft

rate,data = wave.read('son/detection/1.wav')
n = data.size
duree = 1.0*n/rate

te = 1.0/rate
t = np.zeros(n)
for k in range(n):
    t[k] = te*k

entree=data
tps=t
##########

plt.subplot(311)
plt.plot(tps[1000:2000],entree[1000:2000])
plt.title("signal à l'entree du filtre")
plt.grid()

zi = scipy.signal.lfiltic(b2,a2,x=[0],y=[0])
[sortie,zf] = scipy.signal.lfilter(b2,a2,entree,zi=zi)
plt.subplot(312)   
plt.plot(tps[1000:2000],sortie[1000:2000])
plt.title("Signal à la sortie du filtre")
plt.grid()


