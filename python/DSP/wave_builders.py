from numpy import arange
import wave_functions

def sine(freq=2, amp=1, start=0, end=1, fs=44100):
    timeindex = arange(start, end, 1.0/fs)
    return [wave_functions.sine(n, freq, amp) for n in timeindex]

def triangle(freq=2, amp=1, start=0, end=1, fs=44100):
    timeindex = arange(start, end, 1.0/fs)
    return [wave_functions.triangle(n, freq, amp) for n in timeindex]

def triangle2(freq=2, amp=1, start=0, end=1, fs=44100):
    timeindex = arange(start, end, 1.0/fs)
    return [wave_functions.triangle2(n, freq, amp) for n in timeindex]

def sawtooth(freq=2, amp=1, start=0, end=1, fs=44100):
    timeindex = arange(start, end, 1.0/fs)
    return [wave_functions.sawtooth(n, freq, amp) for n in timeindex]

def sawtooth2(freq=2, amp=1, start=0, end=1, fs=44100):
    timeindex = arange(start, end, 1.0/fs)
    return [wave_functions.sawtooth2(n, freq, amp) for n in timeindex]

def square(freq=2, amp=1, start=0, end=1, fs=44100):
    timeindex = arange(start, end, 1.0/fs)
    return [wave_functions.square(n, freq, amp) for n in timeindex]

