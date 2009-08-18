===========
 Debugging
===========

The python debugger ``pdb``: http://docs.python.org/library/pdb.html

A debugger allows you to inspect your code interactively.

You're likely to spend as much time debugging your code as writing it
in the first place.  It pays to learn how to use a debugger.

“Everyone knows that debugging is twice as hard as writing a program
in the first place. So if you're as clever as you can be when you
write it, how will you ever debug it?” (Brian Kernighan)

* Build your code with testing and debugging in mind.
* Don't Repeat Yourself (DRY).  Find duplication in your code and
  encapsulate in a function.
* Keep It Simple, Stupid (KISS).  What is the simplest thing that
  could possibly work?
* Loose coupling
* High Cohesion
* Separation of Concerns

Strategies
^^^^^^^^^^

#. Make it fail reliably.  find a test case that makes the code fail
 every time.
#. Divide and Conquer.  Once you have a failing test case, isolate the
 failing code.
#. Change one thing at a time and re-run the failing test case.
#. Take notes.
#. Be patient.
#. Fernando Perez 1/0 trick.

Debugger allows you to:

  * walk up and down the call stack
  * view the source code
  * inspect values of variables
  * modify values
  * set breakpoints


Ways to launch the debugger:

#. Postmortem, launch debugger after module errors.
#. Enable debugger in ipython and automatically drop into debug-mode
 on error.
#. Launch the module with the debugger.

Postmortem
^^^^^^^^^^






Exercise Ideas:

* typo, using one "1" instead of a lower case "l"
* not importing a module NameError
* referencing a variable before being assigned  NameError
* IndexError, list out of range
* trying to assign immutable


Logging
-------

print
-----


Code Checker
------------

pyflakes: http://pypi.python.org/pypi/pyflakes/0.3.0

Parses the module and checks for logical errors.


testing your code
-----------------

