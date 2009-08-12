===============================================
Introduction to the Python language (Functions)
===============================================

Define a function:

.. sourcecode:: ipython

    In [56]: def foo():
       ....:     print 'in foo function'
       ....:     
       ....:     

    In [57]: foo()
    in foo function

Parameters
----------
Two kinds of parameters:

1) Mandatory parameters (positional arguments)

.. sourcecode:: ipython

    In [81]: def double_it(x):
       ....:     return x * 2
       ....: 

    In [82]: double_it(3)
    Out[82]: 6

    In [83]: double_it(['scipy', 2009])
    Out[83]: ['scipy', 2009, 'scipy', 2009]
   

2) Optional parameters (keyword or named arguments)

.. sourcecode:: ipython

    In [84]: def double_it(x=2):
       ....:     return x * 2
       ....: 

    In [85]: double_it()
    Out[85]: 4

    In [86]: double_it(3)
    Out[86]: 6

Keyword arguments allow you to specify *default values*:

.. sourcecode:: ipython

    In [98]: def slicer(seq, start=None, stop=None, step=None):
       ....:     """Implement basic python slicing."""
       ....:     return seq[start:stop:step]
       ....: 

    In [101]: seq = 'one fish, two fish, red fish, blue fish'.split()

    In [105]: seq
    Out[105]: ['one', 'fish,', 'two', 'fish,', 'red', 'fish,', 'blue', 'fish']

    In [102]: slicer(seq, step=2)
    Out[102]: ['one', 'two', 'red', 'blue']

    In [103]: slicer(seq, 1, step=2)
    Out[103]: ['fish,', 'fish,', 'fish,', 'fish']

    In [104]: slicer(seq, start=1, stop=len(seq), step=2)
    Out[104]: ['fish,', 'fish,', 'fish,', 'fish']

.. warning:: 

   Default values are evaluated when the function is defined, not when
   it is called.

Pass-by-value
-------------

Function parameters are local variables of the function.  Global
variables can be referenced within the function:

.. sourcecode:: ipython

    In [114]: x = 5

    In [115]: def addx(y):
       .....:     return x + y
       .....: 

    In [116]: addx(10)
    Out[116]: 15

But global variables cannot be assigned a value unless declared **global**.

Doesn't work:

.. sourcecode:: ipython

    In [117]: def setx(y):
       .....:     x = y
       .....:     print x
       .....:     
       .....:     

    In [118]: setx(10)
    10

    In [120]: x
    Out[120]: 5

Works:

.. sourcecode:: ipython

    In [121]: def setx(y):
       .....:     global x
       .....:     x = y
       .....:     print x
       .....:     
       .....:     

    In [122]: setx(10)
    10

    In [123]: x
    Out[123]: 10


Variable number of parameters
-----------------------------
Special forms of parameters:
  * \*args: any number of positional arguments packed into a tuple
  * \**kwargs: any number of keyword arguments packed into a dictionary

Cover example from Nutshell where the default value is a mutable
object and the function body alters the parameter?


Return statement
----------------

Functions always return a result, either *None* or a value.


Docstrings
----------

Documention about what the function does and it's parameters.  General
convention:

.. sourcecode:: ipython

    In [67]: def funcname(params):
       ....:     """Concise one-line sentence describing the function.
       ....: 
       ....:     Extended summary which can contain multiple paragraphs.
       ....:     """
       ....:     # function body
       ....:     pass
       ....: 

    In [68]: funcname?
    Type:		function
    Base Class:	<type 'function'>
    String Form:	<function funcname at 0xeaa0f0>
    Namespace:	Interactive
    File:		/Users/cburns/src/scipy2009/.../<ipython console>
    Definition:	funcname(params)
    Docstring:
        Concise one-line sentence describing the function.

        Extended summary which can contain multiple paragraphs.


Functions are objects
---------------------
Functions are first-class objects, which means they can:
  * be assigned to a variable
  * be an item in a list (or any collection)
  * be passed as an argument to another function.


Namespaces
----------


global statement
----------------

