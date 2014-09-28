from mathutils import *
from plotutils import *
import numpy as np

freq      = 2.0
amp       = 0.6
fs        = 44100.0
timeindex = np.arange(0, 1, 1/fs)

def sine(n, freq, amp):
    """
    http://en.wikipedia.org/wiki/Sine_wave
    amp: [-amp, amp]
    """
    return amp * sin(2 * pi * freq * n)

def triangle(n, freq, amp):
    """
    http://en.wikipedia.org/wiki/Triangle_wave
    amp: [-amp, amp]
    """
    return amp * (abs( 4 * ( (n/(1/freq) - 0.25)  % 1 ) - 2 ) - 1)

def triangle2(n, freq, amp):
    """
    http://en.wikipedia.org/wiki/Triangle_wave
    Defined in terms of sine and arcsine 
    amp: [-amp, amp]
    """
    return (2*amp/pi) * arcsin(sin(2*pi/(1/freq)*n))

def sawtooth(n, freq, amp):
    """
    http://en.wikipedia.org/wiki/Sawtooth_wave
    amp: [-amp, amp]
    """
    return amp * (2 * (n/(1/freq) - floor(0.5+(n/(1/freq)))))

def sawtooth2(n, freq, amp):
    """ 
    http://mathworld.wolfram.com/SawtoothWave.html 
    amp: [0, amp]
    """
    return amp * frac(n/(1/freq))

def square(n, freq, amp):
    """ 
    In terms of sine and cosecant.
    http://en.wikipedia.org/wiki/Square_wave
    amp: [-amp, amp]
    """
    return amp * csc(2*pi/(1/freq)*n) * abs(sin(2*pi/(1/freq)*n))

sin1 = [sine(n, freq, amp)       for n in timeindex]
tri1 = [triangle(n, freq, amp)   for n in timeindex]
tri2 = [triangle2(n, freq, amp)  for n in timeindex]
saw1 = [sawtooth(n, freq, amp)   for n in timeindex]
saw2 = [sawtooth2(n, freq, amp)  for n in timeindex]
sqr1 = [square(n, freq, amp)     for n in timeindex]

plot_all(sin1, tri1, tri2, saw1, saw2, sqr1)

