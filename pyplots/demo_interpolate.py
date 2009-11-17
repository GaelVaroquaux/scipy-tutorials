import numpy as np
import pylab as pl
pl.figure(1)
pl.clf()


x = np.arange(10)
y = np.sin(x)

pl.plot(x, y, '+', markersize=10, linewidth=3)

from scipy import interpolate

f = interpolate.interp1d(x, y)
X = np.linspace(0, 9, 100)
pl.plot(X, f(X), '--', linewidth=3)

f = interpolate.interp1d(x, y, kind='cubic')
X = np.linspace(0, 9, 100)
pl.plot(X, f(X), '--', linewidth=3)

