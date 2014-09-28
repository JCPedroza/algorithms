from mathutils import *
import plotutils
import numpy as np
import math

freq      = 2.0
amp       = 0.6
fs        = 44100.0
pi        = np.pi
period    = 1/freq
timeindex = np.arange(0, 1, 1/fs)

def sine(n, freq, amp):
    """
    amp: [-amp, amp]
    """
    return amp * sin(2 * pi * freq * n)

def triangle(n, period, amp):
    """
    amp: [-amp, amp]
    """
    return amp * (abs( 4 * ( (n/period - 0.25)  % 1 ) - 2 ) - 1)

def triangle2(n, period, amp):
    """ 
    Defined in terms of sine and arcsine 
    amp: [-amp, amp]
    """
    return (2*amp/pi) * arcsin(sin(2*pi/period*n))

# Cant make this to be in range [-1, 1]
def sawtooth(n, period, amp):
    """
    amp: [0, amp*2]
    """
    return amp * (2 * (n/period - math.floor((1/2)+(n/period))))

def sawtooth2(n, period, amp):
    """ 
    http://mathworld.wolfram.com/SawtoothWave.html 
    amp: [0, amp]
    """
    return amp * frac(n/period)

def square(n, period, amp):
    """ 
    In terms of sine and cosecant.
    http://en.wikipedia.org/wiki/Square_wave
    amp: [-amp, amp]
    """
    return amp * csc(2*pi/period*n) * abs(sin(2*pi/period*n))

sin1 = [sine(n, freq, amp)         for n in timeindex]
tri1 = [triangle(n, period, amp)   for n in timeindex]
tri2 = [triangle2(n, period, amp)  for n in timeindex]
saw1 = [sawtooth(n, period, amp)   for n in timeindex]
saw2 = [sawtooth2(n, period, amp)  for n in timeindex]
sqr1 = [square(n, period, amp)     for n in timeindex]

plotutils.plot_all(sin1, tri1, tri2, saw1, saw2, sqr1)

