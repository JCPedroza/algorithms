from wave_builders import *
from plotutils import *
import numpy as np

sine1 = sine()
tri1 = triangle()
tri2 = triangle2()
saw1 = sawtooth()
saw2 = sawtooth2()
sqr1 = square()
a_wave = np.convolve(sine1, sqr1)

plot_all(a_wave)