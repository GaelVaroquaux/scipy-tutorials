import numpy as np
import pylab as pl
from scipy import optimize

x = np.linspace(0, 10, 100)
y = np.sin(x) + 0.5*np.random.normal(size=100)

pl.plot(x, y, '.')

def test_func(x, a, f, phi):
    return a*np.sin(f*x+phi)

(a, f, phi), _ = optimize.curve_fit(test_func, x, y)
pl.plot(x, test_func(x, a, f, phi), '--', linewidth=3)

