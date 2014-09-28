import numpy as np
import matplotlib.pyplot as plt
import math

freq      = 2.0
amp       = 0.6
fs        = 44100.0
pi        = np.pi
period    = 1/freq
timeindex = np.arange(0, 1, 1/fs)
def frac(x):
    """ Returns the fractional part of x """
    return x - math.floor(x)

def sine(n, freq, amp):
    return amp * np.sin(2 * pi * freq * n)

def triangle(n, period, amp):
    return amp * (abs( 4 * ( (n/period - 0.25)  % 1 ) - 2 ) - 1)

def triangle2(n, period, amp):
    """ Defined in terms of sine and arcsine """
    return (2*amp/pi) * np.arcsin(np.sin(2*pi/period*n))

# Cant make this to be in range [-1, 1]
def sawtooth(n, period, amp):
    return amp * (2 * (n/period - math.floor((1/2)+(n/period))))

def sawtooth2(n, period, amp):
    """ http://mathworld.wolfram.com/SawtoothWave.html """
    return amp * frac(n/period)

def square(n, period, amp):
    pass

sin1 = [sine(n, freq, amp)         for n in timeindex]
tri1 = [triangle(n, period, amp)   for n in timeindex]
tri2 = [triangle2(n, period, amp)  for n in timeindex]
saw1 = [sawtooth(n, period, amp)   for n in timeindex]
saw2 = [sawtooth2(n, period, amp)  for n in timeindex]


plt.plot(saw2)
plt.plot(saw1)
plt.show()