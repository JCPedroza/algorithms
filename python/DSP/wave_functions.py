from mathutils import *

freq      = 2.0
amp       = 0.6
fs        = 44100.0

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
    return amp * (abs( 4 * ( (n/(1.0/freq) - 0.25)  % 1 ) - 2 ) - 1)

def triangle2(n, freq, amp):
    """
    http://en.wikipedia.org/wiki/Triangle_wave
    Defined in terms of sine and arcsine 
    amp: [-amp, amp]
    """
    return (2*amp/pi) * arcsin(sin(2*pi/(1.0/freq)*n))

def sawtooth(n, freq, amp):
    """
    http://en.wikipedia.org/wiki/Sawtooth_wave
    amp: [-amp, amp]
    """
    return amp * (2 * (n/(1.0/freq) - floor(0.5+(n/(1.0/freq)))))

def sawtooth2(n, freq, amp):
    """ 
    http://mathworld.wolfram.com/SawtoothWave.html 
    amp: [0, amp]
    """
    return amp * frac(n/(1.0/freq))

def square(n, freq, amp):
    """ 
    In terms of sine and cosecant.
    http://en.wikipedia.org/wiki/Square_wave
    amp: [-amp, amp]
    """
    return amp * csc(2*pi/(1.0/freq)*n) * abs(sin(2*pi/(1.0/freq)*n))
