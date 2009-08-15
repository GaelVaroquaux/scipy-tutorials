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
    
    In [5]: from __future__ import braces


Creating modules
-----------------

'__main__'
------------

Standalone scripts
-------------------

command line arguments

