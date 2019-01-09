"""
This module demonstrates lets you practice INPUT from the CONSOLE.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Zhen Yang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ TESTs the functions in this module (by calling them). """
    # double_a_float()
    # print_an_integer_many_times()
    # print_an_integer_many_times_on_one_row()
    input_it_all()


def double_a_float():
    x = float(input('Please enter an float:'))
    x = 2*x
    print(x)
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a floating point number.
       b. Prints the input number, doubled (i.e., multiplied by 2).
    No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colon:
         Enter a number: -3.14
         -6.28
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def print_an_integer_many_times():
    x = int(input('Please enter an positive integer:'))
    a = x * 2
    for k in range(0, x):
        print(a)
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a positive integer.
       b. Prints the input integer, doubled (i.e., multiplied by 2),
          the input number of times.  (See the example.)
    No input validation is required.  Nothing else should be printed.

    Example:
    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         6
         6
         6

         Enter an integer: 5
         10
         10
         10
         10
         10
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def print_an_integer_many_times_on_one_row():
    x = int(input('Please enter an_integer_many_times_on_one_row:'))
    a = x * 2
    b = ''
    for k in range(x):
        b = b + str(a)
    print(b)



    """
    Same as the previous problem, but print the numbers
    on a single line with no spaces in between them.

    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         666

         Enter an integer: 5
         1010101010
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   The testing code is already written for you (above).
    #
    # HINT: One way to print on a SINGLE line is to build up a string
    #       and then print that (single) string.
    # -------------------------------------------------------------------------


def input_it_all():
    a = float(input('A positive floating point number:'))
    b = int(input('A positive integer:'))
    c = str(input('A string'))
    a = a ** 0.5
    for k in range(b):
        print(a)
    for k in range(b):
        print(c)

    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
      Prompts the user for and inputs:
        -- A positive floating point number
        -- A positive integer
        -- A string
      in that order (via three separate INPUT statements).
      Then prints, in this order, all on separate lines:
        a. The square root of the floating point number,
           repeated the input integer number of times.
        b. The string, repeated the input integer number of times.
      No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
