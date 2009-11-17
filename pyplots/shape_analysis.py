import scipy as sp
import numpy as np
import pylab as pl

l = sp.lena()
i = 235
j = 205
l_ = 2*l[i:153+i, j:162+j]

t = pl.imread('tarek1.jpg')
t_ = t.sum(axis=-1)

g = pl.imread('g.jpg')
g_ = g.sum(axis=-1)

################################################################################
pl.gray()
pl.figure(0, figsize=(12, 4.5))
pl.clf()
pl.axes([0, 0, 0.3, 1])
pl.imshow(t_.copy())
pl.axis('off')
pl.axes([0.33, 0, 0.3, 1])
pl.imshow(l_.copy())
pl.axis('off')
#pl.axes([0.66, 0, 0.3, 1])
#pl.imshow(g_.copy())
#pl.axis('off')

t_ = t_.astype(np.float)
#t_ -= t_.mean()
t_ /= t_.max()
#t_ /= np.sqrt((t_**2).sum())

l_ = l_.astype(np.float)
#l_ -= l_.mean()
l_ /= l_.max()
#l_ /= np.sqrt((l_**2).sum())

g_ = g_.astype(np.float)
g_ -= g_.mean()
g_ /= np.sqrt((g_**2).sum())

pl.axes([0.66, 0, 0.3, 1])
pl.imshow(t_ + l_)
pl.axis('off')

################################################################################
pl.figure(1, figsize=(12, 4.5))
pl.clf()
pl.axes([0, 0, 0.3, 1])
u, s, v = np.linalg.svd(t_, full_matrices=False)
t_ = np.dot(u, v)
pl.imshow(t_.copy())
pl.axis('off')

pl.axes([0.33, 0, 0.3, 1])
u, s, v = np.linalg.svd(l_, full_matrices=False)
l_ = np.dot(u, v)
pl.imshow(l_.copy())
pl.axis('off')

#pl.axes([0.66, 0, 0.3, 1])
#u, s, v = np.linalg.svd(g_, full_matrices=False)
#s[50:] = 0
#s[:50] = 1
#g_ = np.dot(u*s, v)
#pl.imshow(g_.copy())
#pl.axis('off')

t_ = t_.astype(np.float)
t_ -= t_.mean()
t_ /= np.sqrt((t_**2).sum())

l_ = l_.astype(np.float)
l_ -= l_.mean()
l_ /= np.sqrt((l_**2).sum())

g_ = g_.astype(np.float)
g_ -= g_.mean()
g_ /= np.sqrt((g_**2).sum())

pl.axes([0.66, 0, 0.3, 1])
pl.imshow(t_ + l_)
pl.axis('off')



