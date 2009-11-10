Reusing code
=============

Importing objects
------------------

  .. sourcecode:: ipython

    In [1]: import os

    In [2]: os
    Out[2]: <module 'os' from '/usr/lib/python2.6/os.pyc'>

    In [3]: os.listdir('.')
    Out[3]: 
    ['conf.py',
     'basic_types.rst',
     'control_flow.rst',
     'functions.rst',
     'python_language.rst',
     'reusing.rst',
     'file_io.rst',
     'exceptions.rst',
     'workflow.rst',
     'index.rst']

And also:

  .. sourcecode:: ipython

    In [4]: from os import listdir

Importing shorthands:

  .. sourcecode:: ipython

    In [5]: import numpy as np

.. warning:: 

    ::
    
      from os import * 

    **Do not do it.**

    * Makes the code harder to read and understand: where do symbols come 
      from?

    * Makes it impossible to guess the functionality by the context and
      the name (hint: `os.name` is the name of the OS), and to profit
      usefully from tab completion.

    * Restricts the variable names you can use: `os.name` might override 
      `name`, or vise-versa.

    * Creates possible name clashes between modules.

    * Makes the code impossible to statically check for undefined
      symbols.

**A whole set of new functionnality!**

  .. sourcecode:: ipython
    
    In [6]: from __future__ import braces


Creating modules
-----------------

File `demo.py`:

  .. literalinclude:: demo.py

Importing it in IPython:

  .. sourcecode:: ipython

    In [6]: import demo

    In [7]: demo?
    Type:		module
    Base Class:	<type 'module'>
    String Form:	<module 'demo' from 'demo.py'>
    Namespace:	Interactive
    File:		/home/varoquau/Projects/Python_talks/scipy_2009_tutorial/source/demo.py
    Docstring:
	A demo module. 


    In [8]: demo.print_a()
    a

    In [9]: demo.print_b()
    b


.. warning:: 

    **Module caching**

     Modules are cached: if you modify `demo.py` and re-import it in the
     old session, you will get the old one.

    Solution:

     .. sourcecode :: ipython

	In [10]: reload(demo)

'__main__' and module loading
------------------------------

File `demo2.py`:

  .. literalinclude:: demo2.py

Importing it:

  .. sourcecode:: ipython

    In [11]: import demo2
    b

    In [12]: import demo2

Running it:

  .. sourcecode:: ipython

    In [13]: %run demo2
    b
    a


Standalone scripts
-------------------

* Running a script from the command line::

    $ python demo2.py
    b
    a

* On Unix, make the file executable: 

    - 'chmod uog+x demo2.py'
    
    - add at the top of the file::

        #!/usr/bin/env python


* Command line arguments::

    import sys
    print sys.argv

  ::

    $ python file.py test arguments
    ['file.py', 'test', 'arguments']

  .. note:: 

    Don't implement option parsing yourself. Use modules such as
    `optparse`.

____

.. topic:: Exercise

    Implement a script that takes a directory name as argument, and
    returns the list of '.py' files, sorted by name length.

    **Hint:** try to understand the docstring of list.sort

:ref:`dir_sort`
