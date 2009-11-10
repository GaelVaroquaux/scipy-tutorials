# -*- coding: utf-8 -*-
ifmain = __name__ == '__main__'

size = 5

image = [[0 for j in range(size)] for i in range(size)] 
image[size/2][size/2] = 1
from copy import deepcopy
image2 = deepcopy(image)
def laplacien():
    for i in xrange(1, size-1):
        for j in xrange(1, size-1):
            image2[i][j] = (image[i+1][j] - image[i-1][j] +
                            image[i][j+1] - image[i][j-1])*0.25
            

# speed of laplacien, measured throught %timeit, on epsilon:
# size = 5,     18.3us
# size = 10,    117us
# size = 50,    3.97ms
# size = 100,   16.6ms
# size = 500,   440ms
# size = 1000,  1.76s
from numpy import r_
sizes = r_[5, 10, 50, 100, 500, 1000]
time_python = r_[18e-6, 120e-6, 4e-3, 17e-3, 0.44, 1.8]
labels_python = [u'18µs', u'120µs', '4.0ms', '17ms', '440ms', '1.8s']

if ifmain:
    laplacien()
from numpy import array
from pylab import pcolor, show, cm, xticks, yticks, figure, savefig, \
                            subplot, clf
image = array(image)

if ifmain:
    figure(2, figsize=(4.5, 2))
    clf()
    subplot(1, 2, 1)
    pcolor(image, cmap=cm.jet, vmin=-1, vmax=1, shading='faceted')
    xticks(())
    yticks(())

    image2 = array(image2)
    subplot(1, 2, 2)
    pcolor(image2, cmap=cm.jet, vmin=-1, vmax=1, shading='faceted')
    xticks(())
    yticks(())
    savefig('laplacien.eps')
    show()

    from enthought.mayavi import mlab 
    mlab.figure(1, size=(720, 300))
    mlab.clf()
    import numpy as np
    x_, y_ = np.indices(image.shape)
    mlab.barchart(x_, y_ - 3, 2*image, vmin=-1, vmax=1)
    mlab.barchart(x_, y_ + 3, 2*image2, vmin=-1, vmax=1)
    mlab.view(0, 63, 8.5, (3, 2, 1))
    mlab.savefig('laplacien.jpg')
    import os
    os.system('mogrify -trim laplacien.jpg')



from numpy import zeros
image  = zeros((size, size))
image[size/2, size/2] = 1

def laplacien_numpy():
    image[1:-1, 1:-1] = (image[:-2, 1:-1] - image[2:, 1:-1] +
                         image[1:-1, :-2] - image[1:-1, 2:])*0.25

# speed of laplacien_numpy, measured throught %timeit, on epsilon:
# size = 5,     38us
# size = 10,    92us
# size = 50,    117us 
# size = 100,   308us
# size = 500,   14.2ms
# size = 1000,  57ms

time_numpy = r_[38e-6, 92e-6, 120e-6, 310e-6, 14e-3, 67e-3]
labels_numpy = [u'38µs', u'92µs', u'120µs', u'310µs', '14ms', '57ms']

if ifmain:
    from pylab import figure, loglog, gca, xlim, ylim, show, ylabel, \
            xlabel, xticks, yticks, text, NullLocator, legend, axes, clf
    figure(1, figsize=(4.5, 2))
    clf()
    ax = axes((0.05, 0.1, 0.8, 0.8))
    loglog(sizes, time_python, '-D', markersize=10, label=u'Python pur')
    loglog(sizes, time_numpy, '-o', markersize=10, label='Numpy')
    ax = gca()

    xlim(1.5, 1000)
    ylim(5e-6, 10)
    xticks(sizes[:-1], ['%i' % n for n in sizes[:-1]])
    show()

    def make_mark(n, t_python, t_numpy, label_python, label_numpy):
        if t_python > t_numpy:
            text(0.87*n, 1.1*t_python, label_python, horizontalalignment='right', 
                            size=11, color=(0, 0, 0.5))
        else:
            text(0.83*n, 0.4*t_python, label_python, horizontalalignment='right', 
                            size=11, color=(0, 0, 0.5))
        if t_python < t_numpy:
            text(0.83*n, 1.1*t_numpy, label_numpy, horizontalalignment='right',
                            size=11, color=(0, 0.25, 0))
        else:
            text(1.8*n-2, 0.14*t_numpy-6e-6, label_numpy, 
                            horizontalalignment='right',
                            size=11, color=(0, 0.25, 0))
            
    from matplotlib.text import FontProperties

    for n, t_python, t_numpy, label_python, label_numpy in \
            zip(sizes, time_python, time_numpy, labels_python, labels_numpy)[:-1]:
        make_mark(n, t_python, t_numpy, label_python, label_numpy)

    ax.xaxis.minor.locator = NullLocator()
    yticks((1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1), 
            (u'10µs', u'100µs', u'1ms', u'10ms', u'100ms', u'1s'))
    ax.yaxis.tick_right()
    ax.yaxis.grid(alpha=0.4)

    for t in ax.xaxis.majorTicks:
        t.tick2line.set_visible(False)

    legend(loc='upper left', numpoints=1, prop=FontProperties(size=12))
    text(2, 1e-6, 'n')

    ylabel(u"Temps d'éxécution")

    savefig('timings.eps')
