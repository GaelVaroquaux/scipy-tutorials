import numpy as np
import scipy as sp
import pylab as pl
l = sp.lena()
pl.figure(1, figsize=(12, 4.5))
pl.gray()
pl.clf()
pl.axes([0, 0, 0.3, 1])
pl.imshow(l)
pl.axis('off')
pl.title('Lena')

pl.axes([0.33, 0, 0.3, 1])
rows, weight, columns = np.linalg.svd(l, full_matrices=False)
l_ = np.dot(rows, columns)
pl.imshow(l_, vmin=0.4*l_.min(), vmax=0.2*l_.max())
pl.axis('off')
pl.title('np.dot(rows, columns)')

pl.axes([0.66, 0, 0.3, 1])
pl.imshow(l[:-2, 1:-1] - l[2:, 1:-1] + l[1:-1, :-2] - l[1:-1, 2:])
pl.axis('off')
pl.title('Laplacien Lena')
