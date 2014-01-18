:orphan:

..  Copyright (C) Paul Resnick, Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Assignments
..  description:: This chapter is where all the assignments for Umich SI 106 are stored.

.. highlight:: python
    :linenothreshold: 500


Week 3: ends January 24
=======================

For this week, you have the following graded activities:

1. Do the multiple choice questions and exercises in the textbook chapters, including the ones at the bottom of the chapters, below the glossary. Don't forget to click **Save** for each of the exercises.

  * Before Tuesday's class:
    * :ref: `Iteration <Iteration>`
  * Before Thursday's class:
    * :ref: `File Input/Output <Files>`

#. Turn in the reading response, by 8 PM the night before your registered section meets.
  
  * Read *The Most Human Human*, Chapter 4, "Site-Specificity vs. Pure Technique"
  * :ref: `Reading response 2 <response_2>`

# Save answers to the exercises in Problem Set 2:
  * :ref: `Problem Set 2 <problem_set_2>`

.. _response_2:


Reading Response
----------------

**Due 8PM the night before your section meets**

Don't forget to click **save**.

1. What did you find particularly interesting in this chapter?  How do you define *site-specificity* based on this reading? When is site-specificity important, and when is it not? What would you like to address in discussion? 

Please write a short paragraph addressing these questions, below.

   .. actex:: rr_2_1
   
      # Fill in your short paragraph answer (about 100-250 words) on the lines between the triple quotes.
      s = """
      
      
      """


.. _problem_set_2:

Problem Set
-----------

**Due:** **Friday, January 24, 5 pm**

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

1. Print out each element of list ``lbc`` on a separate line. Then print the first character of each element on a separate line.

  .. actex:: ps_2_1

    lbc = ["one","four","two","six","nine","eleven"]

    # write code to print each element of list lbc on a separate line

    # write code to print the first character of each element of list lbc on a separate line


#. See comments for instructions, below.

  .. actex:: ps_2_2

      rv = """Once upon a midnight dreary, while I pondered, weak and weary,  
Over many a quaint and curious volume of forgotten lore,  
While I nodded, nearly napping, suddenly there came a tapping,   
As of some one gently rapping, rapping at my chamber door.   
T is some visitor, I muttered, tapping at my chamber door;           5
    Only this and nothing more."""

      # Write code to print the number of characters in the string rv.

      # Write code to print the number of words in the string rv.

      # Write code to find out whether the word "raven" is in the string rv. Print "Yes" if it is, and "No" if it isn't.
      # (For this and the next question, think: what if you couldn't see the whole string value, but you still needed to answer this question?)

      # Write code to find out whether the word "rapping" is in the string rv. Print "Yes" if it is, and "No" if it isn't.


#. Here is a file called ``about_programming.txt``. (It is made up of text from the *Computer Programming* article on Wikipedia; ``http://en.wikipedia.org/wiki/Computer_programming``.) Follow the directions (see the comments in the code window) in the exercises below to manipulate this file.


    .. raw:: html

        <pre id="about_programming.txt">
        Computer programming (often shortened to programming) is a process that leads from an
        original formulation of a computing problem to executable programs. It involves
        activities such as analysis, understanding, and generically solving such problems
        resulting in an algorithm, verification of requirements of the algorithm including its
        correctness and its resource consumption, implementation (or coding) of the algorithm in
        a target programming language, testing, debugging, and maintaining the source code,
        implementation of the build system and management of derived artefacts such as machine
        code of computer programs. The algorithm is often only represented in human-parseable
        form and reasoned about using logic. Source code is written in one or more programming
        languages (such as C++, C#, Java, Python, Smalltalk, JavaScript, etc.). The purpose of
        programming is to find a sequence of instructions that will automate performing a
        specific task or solve a given problem. The process of programming thus often requires
        expertise in many different subjects, including knowledge of the application domain,
        specialized algorithms and formal logic.
        Within software engineering, programming (the implementation) is regarded as one phase in a software development process. There is an on-going debate on the extent to which
        the writing of programs is an art form, a craft, or an engineering discipline. In
        general, good programming is considered to be the measured application of all three,
        with the goal of producing an efficient and evolvable software solution (the criteria
        for "efficient" and "evolvable" vary considerably). The discipline differs from many
        other technical professions in that programmers, in general, do not need to be licensed
        or pass any standardized (or governmentally regulated) certification tests in order to
        call themselves "programmers" or even "software engineers." Because the discipline
        covers many areas, which may or may not include critical applications, it is debatable
        whether licensing is required for the profession as a whole. In most cases, the
        discipline is self-governed by the entities which require the programming, and sometimes
        very strict environments are defined (e.g. United States Air Force use of AdaCore and
        security clearance). However, representing oneself as a "professional software engineer"
        without a license from an accredited institution is illegal in many parts of the world.
        </pre>


    ..actex:: ps_2_3

      # Write code to open the file, about_programming.txt, and save it in a variable, f. 
      # Print the first two lines of the file.


      # Write code to find, and print, the number of lines in the file. 


      # Write code to find, and print, the number of words in the file.


      # Write code to find, and print, the number of characters in the file.


      # Write code to find, and print, the number of lines in the file that include the word "programmer".


      # Write code to find, and print, the number of vowels in the file.



Week 2: ends January 17
=======================

For this week, you have the following graded activities:

1. Do the mutliple choice questions and exercises in the textbook chapters, including the ones at the bottom of the chapters, below the glossary. Don't forget to click Save for each of the exercises.
   
   * Before Tuesday's class: 
      * :ref:`Simple Python Data <simple_python_data>`
      * :ref:`Debugging Interlude <debugging_1>`
   * Before Thursday's class:
      * :ref:`Sequences <sequences_chap>`

#. Turn in the reading response, by 8PM the night before your registered section meets

   * *The Most Human Human*, Chapter 3, "The Migratory Soul"
   * :ref:`Reading response 1 <response_1>`


#. Save answers to the six exercises in Problem Set 1:
   * :ref:`Problem Set 1 <problem_set_1>` 


.. _response_1:

Reading Response
----------------

**Due 8PM the night before your section meets**

Don't forget to click "save" for each of these.

1. If you had to give up either your left-brain functions or your right-brain functions, which would you give up?

   .. actex:: rr_1_1
   
      # Fill in your answer on the lines between the triple quotes
      s = """
      
      
      """
      
#. What's one interesting thing you learned from the chapter? 

   .. actex:: rr_1_2
   
      # Fill in your answer on the lines between the triple quotes
      s = """
      
      
      """

#. What's one question you have or something that you'd like to have discussed during section?

   .. actex:: rr_1_3
   
      # Fill in your answer on the lines between the triple quotes
      s = """
      
      
      """



.. _problem_set_1:

Problem Set
-----------
**Due:** **Friday, January 17, 5 pm**

**Instructions:** Write the code you want to save in the provided boxes, and click **save** for each one. The last code you have saved for each one by the deadline is what will be graded.

1. (1 pt) Given the following code, write a print statement that will pick out the letter ``"o"``, from the string ``s``. 

   .. actex:: ps_1_1

       s = "Hello, all"
	   
	   

#. (1 pt) Write code to print this string WITHOUT any ``&`` signs.

      This is a really fun&& homework assign&ment. And & I love&& &&Python.

   .. actex:: ps_1_2
   
   		# Here's the string provided for you
   		nst = "This is a really fun&& homework assign&ment. And & I love&& &&Python."
		
		# Write your code to print this string without any "&s", below:
		

#. (1 pt) What is the index of the first letter "h" in this sentence? Write code to find it, and print it. (Remember, an index is the __th element of a string or a list, for example.)

      This is a really fun homework assigment, and I love Python.

   .. actex:: ps_1_3
   
   		# Here's the sentence, provided for you
   		st = "This is a really fun homework assigment, and I love Python."
		
		## Write your code to find the first index of the letter "h" below:
   

#. (3 pts) See comments for instructions.

   .. actex:: ps_1_4
		
		abc = [1,2,3,4,5,6,7]
		
		# What is the type of value is in the variable abc? 
		# Write code to find out what type the value of abc is.
		
		## Write the type here: _______
		
		# write code to extract and print the first three elements of abc
		
		# write code to extract and print the last element of abc
		
		# write code to extract and print the number 4 from abc
		
		# write code to extract and print the number 6 from abc
		
		# write code to find out what type the first element of abc is, and print it.



#. (2 pts) See the comments for instructions.

   .. actex:: ps_1_5
   
		xy_lst = ["hello","goodbye","welcome","106","si 106"]
		abc_sentence = "Welcome to SI 106, everyone."
		
		# write code to extract and print the first element of xy_lst
		
		# write code to extract and print the last element of xy_lst
		
		# write code to extract and print the first character of abc_sentence
		
		# write code to extract and print the last character of abc_sentence

			
#. (2 pts) Write code to ask the user for their name and print out ``"Nice to meet you, <THEIR NAME>"``

   .. actex:: ps_1_6
   
		# For example, if you enter "Nick", your code should then print "Nice to meet you, Nick"