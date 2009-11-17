import numpy as np 
import pylab as pl
from scipy.special import jn
x = np.linspace(-5, 15, 100)

for i in range(10):
    y = jn(i, x)
    pl.plot(x, y, label='$j_%i$' % i)

pl.title('Fonctions de Bessel')
pl.legend()

