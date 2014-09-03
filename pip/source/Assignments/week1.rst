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


Week 1: ends September 7
=========================

For this week, you have the following graded activities:

1. Stuff will go here.

#. Save answers to the exercises in Problem Set 1:
   :ref:`Problem Set 1 <problem_set_1>` 

.. _response_1:

Reading Response
----------------

TBA.

.. _problem_set_1:

.. actex:: test_framework
   :nopre:
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
**Due:** **Sunday, September 7th at 5 pm**

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

1. The variable ``tpa`` currently has the value ``0``. Assign the variable ``tpa`` the value ``6`` .

   .. actex:: ps_1_1
      :include: test_framework

      tpa = 0
      
      ====

      print "\n\n---\n"
      testEqual(tpa, 6, "The variable called tpa should hold the value 6 when this code is run.")


#. Write code to assign the variable ``yb`` to have the same value as the variable ``cw``. Do not change the first line of code (``cw = "Hello"``), and do not type or copy/paste ``"Hello"`` again.

   .. actex:: ps_1_2
      :include: test_framework

      cw = "Hello"
      yb = 0

      ====

      print "\n\n---\n"
      testEqual(cw, yb)


#. Write code to print out the type of the variable ``apples_and_oranges``, the type of the variable ``abc``, and the type of the variable ``new_var``.

   .. actex:: ps_1_3
      
      apples_and_oranges = """hello, everybody
                                how're you?"""

      abc = 6.75483

      new_var = 824

      ====

      print "\n\n---\n(There are no tests for this problem.)"


#. There is a function we are giving you called ``square``. It takes one integer and returns the square of that integer value. Write code to assign a variable callex ``xyz`` the integer value ``25``. You should use the square function.

   .. actex:: addl_functions
      :nopre:
      :hidecode:

      def square(num):
         return num**2

      def greeting(st):
         #st = str(st) # just in case
         return "Hello, " + st

      def random_digit():
        import random
        return random.choice([0,1,2,3,4,5,6,7,8,9])
  

   .. actex:: ps_1_4
      :include: addl_functions, test_framework

      # Want to make sure there really is a function called square? Uncomment the following line and press run.

      #print type(square)

      xyz = ""
      
      ====

      print "\n\n---\n"
      testType(xyz,"int", "The type of the value in variable xyz should be an int")
      testEqual(xyz,25,"The value of the variable xyz should be 25")
      

#. Write code to assign the return value of the function call ``square(3)`` to the variable ``new_number``.

    .. actex:: ps_1_5
       :include: addl_functions, test_framework


       ====

       print "\n\n---\n"
       new_number = None
       if new_number:
          testEqual(new_number, square(3))
       else:
          print "Failed test: the variable new_number does not exist yet"


#. Write in a comment what each line of this code does. 

    .. actex:: ps_1_6
       :include: test_framework, addl_functions

       # Here's an example.
       xyz = 12 # The variable xyz is being assigned the value 12, which is an integer

       # Now do the same for these!
       a = 6

       b = a

       # make sure to be very clear and detailed about the following line of code
       orange = square(b)

       print a

       print b

       print orange

       pear = square

       print pear

#. There are a couple more functions we're giving you in this problem set. One is a function called ``greeting``, which takes any string and adds ``"Hello, "`` in front of it. (You can see examples in the code.) Another one is a function called ``random_digit``, which returns a value of any random integer between 0 and 9 (inclusive). (You can also see examples in the code.)

  Write code that assigns the variable ``func_var`` the value of the **function** ``greeting``. 

  Then, write code that assigns the variable ``new_digit`` to the **return value** of the function ``random_digit``.

  Then, write code that assigns the variable ``digit_func`` to the value of the **function** ``random_digit``.


    .. actex:: ps_1_7
      :include: addl_functions, test_framework

      # For example
      print greeting("Jackie")
      print greeting("everybody")
      print greeting("sdgadgsal")
      
      # Try running all this code more than once, so you can see how calling the function
      # random_digit works.
      print random_digit()
      print random_digit()

      # Write code that assigns the variables as mentioned in the instructions below this line.

      ====

      print "\n\n---\n"
      testType(func_var,"function", "The variable func_var should be assigned the value of the function once this code is run")
      testType(new_digit, "int")
      testType(digit_func, "function")

#. Now write code that assigns the variable ``newval`` to hold the **return value** of ``greeting("everyone in class")``.

    .. actex:: ps_1_8
      :include: addl_functions, test_framework

      ====

      print "\n\n---\n"
      testEqual(newval, greeting("everyone in class"))
    

#. This code causes an error. Why? Write a comment explaining.

    .. actex:: ps_1_9
      :include: addl_functions, test_framework

      another_variable = "?!"
      b = another_variable()
