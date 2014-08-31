:orphan:

..  Copyright (C) Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. highlight:: python
    :linenothreshold: 500


Week 1: ends **DATE**
=======================

For this week, you have the following graded activities:

1. Stuff will go here.

#. Save answers to the exercises in Problem Set 1:
   :ref:`Problem Set 1 <problem_set_1>` 


.. _response_1:

Reading Response
----------------

Coming soon.

.. _problem_set_1:

.. actex:: test_framework
   :hidecode:
   
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


Problem Set
-----------
**Due:** **TBA**

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

1. The variable ``tpa`` currently has the value ``0``. Assign the variable ``tpa`` the value ``6`` .

   .. actex:: ps_1_1
      :include: test_framework

      tpa = 0
      
      ====

      testEqual(tpa, 6, "The variable called tpa should hold the value 6 when this code is run.")


#. Write code to assign the variable ``yb`` to have the same value as the variable ``cw``. Do not change the first line of code (``cw = "Hello"``), and do not type or copy/paste ``"Hello"`` again.

   .. actex:: ps_1_2
      :include: test_framework

      cw = "Hello"
      yb = 0

      ====

      testEqual(cw, yb)


#. Write code to print out the type of the variable ``apples_and_oranges``.

   .. actex:: ps_1_3


#. There is a function we are giving you called ``square``. It takes one integer and returns the _square_ of that integer value. Write code to assign a variable callex ``xyz`` the integer value ``25``. You should use the square function.

   .. actex:: square_function
      :hidecode:

      def square(num):
         return num**2

   .. actex:: ps_1_4
      :include: square_function, test_framework

      xyz = ""
      
      ====

      testType(xyz,"int", "The type of the value in variable xyz should be an int")
      testEqual(xyz,25,"The value of the variable xyz should be 25")
      

