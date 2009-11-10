
from enthought.mayavi import mlab
import numpy as np

class NewFig():
    n = 0
    def __call__(self, **options):
        my_options = dict(size=(400, 300), bgcolor=(1, 1, 1), 
                          fgcolor=(0, 0, 0), )
        my_options.update(options)
        mlab.figure(self.n, **my_options)
        mlab.clf()
        self.n += 1

new_fig = NewFig()

options = dict(scale_factor=0.9, mode='cube', scale_mode='none',
                                 vmin=0, vmax=10, opacity=0.3)

################################################################################
# Broadcasting first figure
################################################################################
new_fig()

a = 0*np.ones((8, 5, 3), np.int)
a = np.atleast_3d(a)
x, y, z = -np.indices(a.shape)
z *= -1
mat1 = mlab.points3d(x, y, z, a, **options)
mlab.outline(mat1)

a = 10*np.ones((8, 1, 1), np.int)
a = np.atleast_3d(a)
x, y, z = -np.indices(a.shape)
y += 2
z *= -1
mat2 = mlab.points3d(x, y, z, a, **options)
o = mlab.outline(mat1)
mlab.pipeline.set_extent(o, mat2.actor.actor.bounds)

a = 5*np.ones((1, 5, 3), np.int)
a = np.atleast_3d(a)
x, y, z = -np.indices(a.shape)
x += 2
z *= -1
mat3 = mlab.points3d(x, y, z, a, **options)
o = mlab.outline(mat1)
mlab.pipeline.set_extent(o, mat3.actor.actor.bounds)

mlab.view(45, 54.7, 16.4, [-2, -1.26,  0.748])
mlab.savefig('broadcasting.jpg')

################################################################################
# 3D cube of x**2 + y**2 + z**2 
################################################################################
new_fig(size=(300, 300))

options['opacity'] = 1

x, y, z = np.ogrid[0:4, 0:4, 0:4]
r = 2*np.sqrt(x**2 + y**2 + z**2)
pts = mlab.points3d(r, **options)

mlab.view(-96, 46, 11.2)
mlab.savefig('3d_radius.jpg')

################################################################################
# Non-broadcasting version of the cube calculation 
################################################################################
new_fig(size=(500, 300))

options['opacity'] = 1

x, y, z = np.mgrid[0:4, 0:4, 0:4]

pts_x = mlab.points3d(x-5, y, z, 2*z, **options)
pts_y = mlab.points3d(x-10, y, z, 2*y, **options)
pts_z = mlab.points3d(x-15, y, z, 2*x, **options)

r = 2*np.sqrt(x**2 + y**2 + z**2)
pts = mlab.points3d(r, **options)

mlab.text(-14.5, -1, 'x', z=-3, width=0.06)
mlab.text(-9.2, -1, 'y', z=-3, width=0.06)
mlab.text(-4, -1, 'z', z=-3, width=0.05)
mlab.text(1.5, -1, 'r', z=-3, width=0.035)

mlab.view(-96, 46, 22, (-6.25, 1.1, 1.1))
mlab.savefig('3d_radius_non_broadcasting.jpg')

################################################################################
# Broadcasting operations that happen in this cube 
################################################################################

x, y, z = np.mgrid[0:4, 0:4, 0:4]

mlab.outline(pts_x, color=(0.5, 0.5, 0.5))
pts_x.remove()
mlab.outline(pts_y, color=(0.5, 0.5, 0.5))
pts_y.remove()
mlab.outline(pts_z, color=(0.5, 0.5, 0.5))
pts_z.remove()

mlab.points3d(-5*np.ones_like(z), np.zeros_like(z), z, 2*z, **options)
mlab.points3d(-10*np.ones_like(y), y, np.zeros_like(y), 2*y, **options)
mlab.points3d(x-15, np.zeros_like(x), np.zeros_like(x), 2*x, **options)

r = 2*np.sqrt(x**2 + y**2 + z**2)
pts = mlab.points3d(r, **options)

mlab.text(-14.5, -1, 'x', z=-3, width=0.06)
mlab.text(-9.2, -1, 'y', z=-3, width=0.06)
mlab.text(-4, -1, 'z', z=-3, width=0.05)
mlab.text(1.5, -1, 'r', z=-3, width=0.035)

mlab.view(-96, 46, 22, (-6.25, 1.1, 1.1))

mlab.savefig('3d_radius_broadcasting.jpg')

################################################################################
# Local average 
################################################################################
new_fig(size=(300, 300))

options['opacity'] = 1

a = np.ones((8, 4))
indices = np.arange(4)
a[indices, indices]
pts = mlab.points3d(a, **options)

mlab.savefig('running_average.jpg')


