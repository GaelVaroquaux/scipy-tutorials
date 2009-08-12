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


Functions are first-class objects: 
  * can be bound to a value 
  * an item in a list
  * passed as an argument to another function.

Function parameters are local variables of the function.  Can
reference global variables within the function but global variables
cannot be assigned a value unless declared **global**.


mandatory parameters vs. optional parameters (with default values)

.. warning:: 

   Default values are evaluated when the function is defined, not when
   it is called.

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


