===========================================
Python patterns in neuro image
===========================================

Images and Mask
================

An fMRI dataset: 4D array, (x, y, z, t) ::

  im = np.random.random((8, 9, 10, 11))

A mask (ROI, or brain): 3D array, (x, y, z) ::

  mask = (np.random.random((8, 9, 10)) > .5)

Corresponding time series: 2D array, (voxel, t) ::

  time_series = im[mask]

Memory management
==================

* In place operations::

    time_series -= time_series.mean(axis=-1)[:, np.newaxis]
    time_series /= time_series.std(axis=-1)[:, np.newaxis]

* For loops rather than axis::

    from scipy import signal

    for time_serie in time_series:
	time_serie[:] = signal.detrend(time_serie)

  .. note::
  
    `time_serie` is a view on `time_series`. `time_serie[:]` gives an
    in-place operation.

* memmapping (np.load)::

    np.save('time_series.npy', time_series)
    time_series = np.load('time_series.npy', mmap_mode='r')

  .. warning::
  
    memmap object: read-only


Masked arrays
================

Data, with many dimensions/parameters: subject, session, ROI, time::

  data = np.ones((3, 4, 10)) # subject, ROI, time

But: **missing data**, **crapy data**, (babies anyone?)::

  bad_data = np.zeros(data.shape, dtype=np.bool)
  # For subject 0, ROI 1 is outside of brain
  bad_data[0, 1, :] = True
  # Subject 1 moved between time 3 and 5:
  bad_data[1, :, 3:6] = True

"Mask" the bad data: masked arrays (`np.ma`)::

  good_data = np.ma.masked_array(data, mask=bad_data)

How many useful ROIs::

  >>> good_data.sum(axis=1)
  masked_array(data =
  [[3.0 3.0 3.0 3.0 3.0 3.0 3.0 3.0 3.0 3.0]
  [4.0 4.0 4.0 -- -- -- 4.0 4.0 4.0 4.0]
  [4.0 4.0 4.0 4.0 4.0 4.0 4.0 4.0 4.0 4.0]],
      	mask =
  [[False False False False False False False False False False]
  [False False False  True  True  True False False False False]
  [False False False False False False False False False False]],
	fill_value = 1e+20)

What's the mean across time, not counting bad data::

  masked_array(data =
    [[1.0 -- 1.0 1.0]
    [1.0 1.0 1.0 1.0]
    [1.0 1.0 1.0 1.0]],
                mask =
    [[False  True False False]
    [False False False False]
    [False False False False]],
          fill_value = 1e+20)


.. note:: Much better than NaNs, the above would not be possible.

.. note::

  Also good for thresholding maps.


Dealing with labels
===================

* ndimage.labels::

    l = sp.lena()[200:300, 230:360]
    pl.imshow(l, cmap=pl.cm.gray)

 .. image:: lena_eyes.png
    :scale: 50

 ::

    blacks = l < 80
    pl.imshow(blacks, cmap=pl.cm.gray)

 .. image:: lena_blacks.png
    :scale: 50

 ::
    
    from scipy import ndimage
    label_im, labels = ndimage.label(blacks)
    imshow(label_im, cmap=pl.cm.spectral)

 .. image:: lena_labels.png
    :scale: 50


* ndimage.mean, ndimage.maximum, ndimage.maximum_position...::

    means = ndimage.mean(l, labels=label_im, index=range(labels))

  Clean up small connect components::

    labels = np.arange(labels)
    size = ndimage.sum(blacks, labels=label_im, index=labels)
    for s, index in zip(size, labels):
	if s < 40:
	   label_im[label_im == index] = 0

 .. image:: lena_pruned.png
    :scale: 50


* Reassign labels np.searchsorted::

    labels = np.unique(label_im)
    label_im = np.searchsorted(labels, label_im)

 .. image:: lena_searchsorted.png
    :scale: 50

* ndimage.center_of_mass::

    >>> ndimage.center_of_mass(label_im.astype(np.float), 
			    label_im.astype(np.float), index=labels)
    [(nan, nan),
    (14.303212851405622, 8.6425702811244989),
    (6.0357142857142856, 24.910714285714285),
    (62.170854271356781, 33.984924623115575),
    (nan, nan),
    (nan, nan)]

* ndimage.find_objects::

    slice_x, slice_y = ndimage.find_objects(label_im==4)[0]
    eye = l[slice_x, slice_y]
    pl.imshow(eye, cmap=pl.cm.gray)

  .. image:: the_eye.png
    :scale: 50

