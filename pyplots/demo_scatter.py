import numpy as np 
import pylab as pl
x, y, value = np.random.normal(size=(3, 50))
pl.scatter(x, y, np.abs(50*value), c=value)
