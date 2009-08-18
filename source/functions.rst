Defining functions
=====================

Function definition
-------------------

.. sourcecode:: ipython

    In [56]: def foo():
       ....:     print 'in foo function'
       ....:     
       ....:     

    In [57]: foo()
    in foo function

Return statement
----------------

Functions can *optionally* return values.

.. sourcecode:: ipython

    In [6]: def area(radius):
       ...:     return 3.14 * radius * radius
       ...: 

    In [8]: area(1.5)
    Out[8]: 7.0649999999999995

.. Note:: By default, functions return ``None``.

Parameters
----------

Mandatory parameters (positional arguments)

.. sourcecode:: ipython

    In [81]: def double_it(x):
       ....:     return x * 2
       ....: 

    In [82]: double_it(3)
    Out[82]: 6

    In [83]: double_it()
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    /Users/cburns/src/scipy2009/scipy_2009_tutorial/source/<ipython console> in <module>()

    TypeError: double_it() takes exactly 1 argument (0 given)

Optional parameters (keyword or named arguments)

.. sourcecode:: ipython

    In [84]: def double_it(x=2):
       ....:     return x * 2
       ....: 

    In [85]: double_it()
    Out[85]: 4

    In [86]: double_it(3)
    Out[86]: 6

Keyword arguments allow you to specify *default values*.

.. warning:: 

   Default values are evaluated when the function is defined, not when
   it is called.

.. sourcecode:: ipython

    In [124]: bigx = 10

    In [125]: def double_it(x=bigx):
       .....:     return x * 2
       .....: 

    In [126]: bigx = 1e9  # No big

    In [128]: double_it()
    Out[128]: 20

More involved example implementing python's slicing:

.. sourcecode:: ipython

    In [98]: def slicer(seq, start=None, stop=None, step=None):
       ....:     """Implement basic python slicing."""
       ....:     return seq[start:stop:step]
       ....: 

    In [101]: seuss = 'one fish, two fish, red fish, blue fish'.split()

    In [102]: seuss
    Out[102]: ['one', 'fish,', 'two', 'fish,', 'red', 'fish,', 'blue', 'fish']

    In [103]: slicer(seuss)
    Out[103]: ['one', 'fish,', 'two', 'fish,', 'red', 'fish,', 'blue', 'fish']

    In [104]: slicer(seuss, step=2)
    Out[104]: ['one', 'two', 'red', 'blue']

    In [105]: slicer(seuss, 1, step=2)
    Out[105]: ['fish,', 'fish,', 'fish,', 'fish']

    In [106]: slicer(seuss, start=1, stop=4, step=2)
    Out[106]: ['fish,', 'fish,']


Passed by value
---------------

Parameters to functions are passed by value.

When you pass a variable to a function, python passes the object to
which the variable refers (the **value**).  Not the variable itself.

If the **value** is immutable, the function does not modify the
caller's variable.  If the **value** is mutable, the function modifies
the caller's variable.

.. sourcecode:: ipython

    In [1]: def foo(x, y):
       ...:     x = 23
       ...:     y.append(42)
       ...:	print 'x is', x
       ...:	print 'y is', y
       ...:     

    In [2]: a = 77    # immutable variable

    In [3]: b = [99]  # mutable variable

    In [4]: foo(a, b)
    x is 23
    y is [99, 42]

    In [5]: print a
    77

    In [6]: print b    # mutable variable 'b' was modified
    [99, 42]

Functions have a local variable table. Called a *local namespace*.

The variable ``x`` only exists within the function *foo*.


Global variables
----------------

Variables declared outside the function can be referenced within the
function:

.. sourcecode:: ipython

    In [114]: x = 5

    In [115]: def addx(y):
       .....:     return x + y
       .....: 

    In [116]: addx(10)
    Out[116]: 15

But these "global" variables cannot be modified within the function,
unless declared **global** in the function.

This doesn't work:

.. sourcecode:: ipython

    In [117]: def setx(y):
       .....:     x = y
       .....:     print 'x is', x
       .....:     
       .....:     

    In [118]: setx(10)
    x is 10

    In [120]: x
    Out[120]: 5

This works:

.. sourcecode:: ipython

    In [121]: def setx(y):
       .....:     global x
       .....:     x = y
       .....:     print 'x is', x
       .....:     
       .....:     

    In [122]: setx(10)
    x is 10

    In [123]: x
    Out[123]: 10


Variable number of parameters
-----------------------------
Special forms of parameters:
  * \*args: any number of positional arguments packed into a tuple
  * \**kwargs: any number of keyword arguments packed into a dictionary

.. sourcecode:: ipython

    In [35]: def variable_args(*args, **kwargs):
       ....:     print 'args is', args
       ....:     print 'kwargs is', kwargs
       ....: 

    In [36]: variable_args('one', 'two', x=1, y=2, z=3)
    args is ('one', 'two')
    kwargs is {'y': 2, 'x': 1, 'z': 3}


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
Functions are first-class objects, which means they can be:
  * assigned to a variable
  * an item in a list (or any collection)
  * passed as an argument to another function.

.. sourcecode:: ipython

    In [38]: va = variable_args

    In [39]: va('three', x=1, y=2)
    args is ('three',)
    kwargs is {'y': 2, 'x': 1}


Methods
-------

Methods are functions attached to objects.  You've seen these in our
examples on **lists**, **dictionaries**, **strings**, etc...


.. topic:: Exercise

    Implement the quicksort algorithm, as defined by wikipedia::

	function quicksort(array)
	    var list less, greater
	    if length(array) ≤ 1  
		return array  
	    select and remove a pivot value pivot from array
	    for each x in array
		if x ≤ pivot then append x to less
		else append x to greater
	    return concatenate(quicksort(less), pivot, quicksort(greater))


