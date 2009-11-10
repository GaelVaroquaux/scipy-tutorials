Timeit
========

Dans IPython, pour timer des opérations élementaires:

.. sourcecode:: ipython
    
    In [1]: import numpy as np

    In [2]: a = np.arange(1000)

    In [3]: %timeit a**2
    100000 loops, best of 3: 5.73 us per loop

    In [4]: %timeit a**2.1
    1000 loops, best of 3: 154 us per loop

    In [5]: %timeit a*a
    100000 loops, best of 3: 5.56 us per loop


    

