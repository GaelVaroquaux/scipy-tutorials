======================
 Timing and Profiling
======================

Timing your code
----------------

.. Note:: The timeit module: http://docs.python.org/library/timeit.html

Use ``timeit`` to measure the execution time of code.

.. sourcecode:: ipython

    In [98]: %timeit [x+3 for x in range(10)]
    100000 loops, best of 3: 3.91 us per loop

You can specify the number of times to execute the statement in a loop:

.. sourcecode:: ipython

    In [99]: %timeit -n 10 [x+3 for x in range(10)]
    10 loops, best of 3: 8.82 us per loop

Compare the execution time of different functions:

.. sourcecode:: ipython

    In [103]: def slow(x):
       .....:     result = []
       .....:     for item in x:
       .....:         result.insert(0, item)
       .....:     return result
       .....: 

    In [104]: def fast(x):
       .....:     result = []
       .....:     for item in x:
       .....:         result.append(item)
       .....:     result.reverse()
       .....:     return result
       .....: 

    In [105]: %timeit slow(range(100))
    10000 loops, best of 3: 64.6 us per loop

    In [106]: %timeit fast(range(100))
    10000 loops, best of 3: 34.1 us per loop


Profiling your code
-------------------

The profile module: http://docs.python.org/library/profile.html

.. sourcecode:: ipython

    In [4]: import cProfile

    In [5]: cProfile.runctx('slow(range(100))', globals(), locals())
             104 function calls in 0.000 CPU seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 tmp.py:128(slow)
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
          100    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
            1    0.000    0.000    0.000    0.000 {range}

Line profiling
--------------

Robert Kern wrote tool to profile each line of your function.

line_profiler: http://pypi.python.org/pypi/line_profiler

Add the ``@profile`` decorator to your function and execute the module:::

    kernprof.py -lv module_name.py

    cburns@source 16:42:19 $ kernprof.py -lv profiler.py
    Wrote profile results to profiler.py.lprof
    Timer unit: 1e-06 s

    File: profiler.py
    Function: slow at line 10
    Total time: 0.000351 s

    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
        10                                           @profile
        11                                           def slow(x):
        12         1            3      3.0      0.9      result = []
        13       101          145      1.4     41.3      for item in x:
        14       100          201      2.0     57.3          result.insert(0, item)
        15         1            2      2.0      0.6      return result


