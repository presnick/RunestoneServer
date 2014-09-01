..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Introduction: Test Cases Revisited
====================

Previously, you were introduced to the idea of test cases. Take a few minutes to :ref:`review that chapter <simple_tests_chap>` if you don't remember it.

Python provides a unit testing framework. It makes it easy to keep track of all your tests and to run them all whenever you make changes to your code, to make
sure that new code you've written hasn't made any of the tests fail that previously passed. We are not going to learn to use that framework. It's overkill for the learning objectives of this couse, which are just trying to introduce you to the main idea of unit testing.

Instead, we have provided a modified version of the simple testing module that you have previously imported. Its full code is shown below and it has been distributed in the inclass/ folder. In this chapter, we will use it to dicuss how to write good test cases.


.. sourcecode:: python
   
   i = 0
   
   def testEqual(actual, expected, feedback = ""):
       global i
       i += 1
       print "--",
       if type(expected) != type(actual):
           print "Failed test %d: %s\n\ttype of expected and actual don't match" % (i, feedback)
           return False
       if type(expected) == type(1):
           # they're integers, so check if exactly the same
           if actual == expected:
               print'Pass test %d: %s'  % (i, feedback)
               return True
       elif type(expected) == type(1.11):
           # a float is expected, so just check if it's very close, to allow for
           # rounding errors
           if abs(actual-expected) < 0.00001:
               print'Pass test %d: %s'  % (i, feedback)
               return True
       elif type(expected) == type([]):
           if len (expected) != len(actual):
               print "Failed test %d: %s\n\tLengths don't match" % (i, feedback)
               return False
           else:
               for (x, y) in zip(expected, actual):
                   if x != y:
                       print "Failed test %d: %s\n\titems in expected and actual do not match" % (i, feedback)
                       return False
               print'Pass test %d: %s'  % (i, feedback)
               return True
       else:
           # check if they are equal
           if actual == expected:
               print'Pass test %d: %s'  % (i, feedback)
               return True
       print 'Failed test %d: %s\n\texpected:\t%s\n\tgot:\t\t%s' % (i, feedback, expected, actual)
       return False
   
   def testType(actual, typeName, feedback = ""):
       global i
       i = i+1
       print "--",
       types = {"string": type(""),
                "dictionary": type({}),
                "list": type([]),
                "int": type(1),
                "float": type(1.0),
                "None": type(None),
                "function": type(lambda x: x)
                }
       if typeName not in types.keys():     
           print('Failed test %d: %s\n\tunknown typeName %s specified.\n\tShould be one of %s' % (i, feedback, typeName, types.keys()))
           return False
       else:
           expected = types[typeName]
       if type(actual) == expected:
           print'Pass test %d: %s'  % (i, feedback)
           return True
       else:
           print('Failed test %d: %s\n\texpected type %s\n\tgot %s' % (i, feedback, expected, type(actual)))
           return False

Compared to the original version of the test module, the key changes are:

* The pass or fail messages are labeled with an index i, so you keep track of which tests are passing and failing. The first test that is run is automatically labeled 1, the second 2, and so on.
* To further aid you in finding which test is failing, in addition to the automatically generated number, a text string named ``feedback`` is also printed out. This is an optional parameter that is specified when the test function is invoked.
* A few improvements have been made in the testEqual function to give you better diagnostics about what's wrong when the expected and actual values are not equal.
* A new function is included, ``testType``. It checks whether a value is of a specified type. The types are specified by a the parameter ``typeName``, which takes one of the following values: "string", "dictionary", "list", "int", "float", "None", or "function".

The testType function isn't really needed. Instead of calling ``test.testType(x, "int")``, you could get the same effect with ``test.testEqual(type(x), type(1))``. The testType function is provided just because it's a little clearer for a person reading  ``test.testType(x, "int")`` to understand what it is doing.

Writing Test Cases
==================

It is a good idea to write one or more test cases for each function, method, or class that you define. We will start with functions and then move on to classes.

