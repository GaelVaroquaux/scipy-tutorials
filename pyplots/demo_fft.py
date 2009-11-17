import numpy as np
import pylab as pl
from scipy import fftpack

t = np.arange(0, 10, 0.1)

s = np.sin(np.pi*t) + np.cos(10*np.pi*t)

pl.plot(t, s)

freq = fftpack.fftfreq(len(s), d=.1)
fft = fftpack.fft(s)
fft[np.abs(freq) > 1] = 0
s_ = fftpack.ifft(fft)

pl.plot(t, s_, linewidth=3)
