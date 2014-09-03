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


Week 2: ends Sunday, September 14
=================================

For this week, you have the following graded activities:

#. Save answers to the exercises in Problem Set 2:
   :ref:`Problem Set 2 <problem_set_2>` 


.. actex:: test_framework_2
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

.. actex:: addl_functions_2
    :nopre:
    :hidecode:

    import turtle

    def add_lengths(s1,s2):
        return len(s1) + len(s2)

    def random_digit():
        import random
        return random.choice([0,1,2,3,4,5,6,7,8,9])

    def square(x):
        return x**2


.. _problem_set_2:

Problem Set
-----------
**Due:** **Sunday, September 14th at 5 pm**

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

1. Assign the variable ``fl`` the value of the first element of the string value in ``original_str``. Assign the variable ``last_l`` the value of the last element of the string value in ``original_str``.

   .. actex:: ps_2_1
      :include: test_framework_2

      original_str = "The quick brown rhino jumped over the extremely lazy fox."

      # assign variables as specified below this line!

      ====

      print "\n\n---\n"
      testEqual(fl,original_str[0], "the value of the var fl and the first element of original_str should be equal")
      testEqual(last_l, original_str[-1], "the value of the var last_l and the last element of original_str should be equal")

#. See comments for instructions.

    .. actex:: ps_2_2
        :include: test_framework_2

        sent = """
        He took his vorpal sword in hand:
        Long time the manxome foe he sought
        So rested he by the Tumtum tree,
        And stood awhile in thought.
        - Jabberwocky, Lewis Carroll (1832-1898)"""

        short_sent = """
        So much depends
        on
        """

        # How long (how many characters) is the string in the variable sent?
        # Write code to assign the length of the string to a variable called len_of_sent.


        # How long is the string in the variable short_sent?
        # Write code to assign the length of that string to a variable called short_len.


        # Print out the value of short_len (and len_of_sent, if you want!) so you can see it. 


        # Write a comment below this line to explain why these values are larger than you might expect. Why is the length of short_sent longer than 15 characters?


        # Assign the index of the first 'v' in the value of the variable sent TO a variable called index_of_v. (Hint: we saw a function built into Python that can help with this)

        ====

        print "\n\n---\n"
        testEqual(len_of_sent,len(sent))
        testEqual(short_len,len(short_sent))
        testEqual(index_of_v, sent.find('v'))



#. See comments for instructions again. (Keep in mind: All ordinal numbers in *instructions*, like "third" or "fifth" refer to the way HUMANS count. How do you write code to find the right things?)

    .. actex:: ps_2_3
        :include: test_framework_2

        num_lst = [4,16,25,9,100,12,13]
        mixed_bag = ["hi", 4,6,8, 92.4, "see ya", "23", 23]

        # Assign the value of the third element of num_lst to a variable called third_elem

        # Assign the value of the sixth element of num_lst to a variable called elem_sixth

        # Assign the length of num_lst to a variable called num_lst_len

        # Write a comment explaining the difference between mixed_bag[-1] and mixed_bag[-2]
        # (you may want to print out those values so you can make sure you know what they are!)

        # Write code to print out the type of the third element of mixed_bag

        # Write code to assign the **type of the fifth element of mixed_bag** to a variable called fifth_type

        # Write code to assign the **type of the first element of mixed_bag** to a variable called another_type

        ====

        print "\n\n---\n"
        testEqual(third_elem, num_lst[2])
        testEqual(elem_sixth, num_lst[5])
        testEqual(num_lst_len,len(num_lst_len))
        testEqual(fifth_type,type(mixed_bag[4]))
        testEqual(another_type, type(mixed_bag[0]))


#. There is a function we are giving you for this problem set that takes two strings, and returns the length of both of those strings added together, called ``add_lengths``. We are also including the functions from Problem Set 1 called ``random_digit`` and ``square`` in this problem set. 

    Now, take a look at the following code and related questions, in this code window.

    .. actex:: ps_2_4
        :include: addl_functions_2

        new_str = "'Twas brillig"

        y = add_lengths("receipt","receive")

        x = random_digit()

        z = new_str.find('b')

        l = new_str.find("'")

        # notice that this line of code is made up of a lot of different expressions
        fin_value = square(len(new_str)) + (z - l) + (x * random_digit())

        # DO NOT CHANGE ANY CODE ABOVE THIS LINE
        # But below here, putting print statements and running the code may help you!


        # The following questions are based on that code. All refer to the types of the 
        #variables and/or expressions after the above code is run.

        #####################   

        # Write a comment explaining each of the following, after each question.
        # Don't forget to save!

        # What is square? 

        # What type of expression is square(len(new_str))? What type will that evaluate to?

        # What type is z?

        # What type is l?

        # What type is the expression z-l?

        # What type is x?

        # What is random_digit? How many inputs does it take?

        # What type does the expression (x * random_digit()) evaluate to?

        # Given all this information, what type will fin_value hold once all this code is run?


#. Here's another complicated expression, using the Turtle framework we talked about. Write comments to answer the questions that follow the code. You may want to write additional code expressions, like printing the type of different variables (e.g. ``print type(x)``) to help you.)

   .. actex:: ps_2_5
      :include: addl_functions_2

      turtle = Turtle()
      x = random_digit() + 1
      turtle.speed = 3
      turtle.move(square(x*turtle.speed))

      # Think about what happens as this code is run, in what order it gets interpreted.
      # Write some code statements to help you think about this, like mentioned in directions.


      # Then answer these questions, each in a comment:

      # What type is the variable turtle?

      # What type is the variable x?

      # What type is the expression turtle.speed?

      # What type is turtle.move? What does that mean?

      # What is square? How many inputs does it take?

      # What type is x * turtle.speed?

      # What type does square(x*turtle.speed) evaluate to?



      
