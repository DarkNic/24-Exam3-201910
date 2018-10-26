"""
Exam 3, problem 2.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Nicolas Bohner.  October 2018.

"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper
import math as m


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2()


def run_test_problem2():
    """ Tests the  problem2   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2   function:')
    print('--------------------------------------------------')

    format_string = '    problem2( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [9, 88, 2, -1, 5, 17, 4]
    expected = 1
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [9, 13, 2, -1, 5, 17, 4]
    expected = 5
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [9, -88, 2, -1, 5, 17, 4]
    expected = 1
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [-500]
    expected = 0
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = [1, 2, 3, 4, 5, 6, 7, -500]
    expected = 7
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem2(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)
    
    
def problem2(sequence):
    """
    What comes in:
      -- An non-empty sequence of integers with no duplicates.
    What goes out:
      -- Returns the index of the number in the sequence
           whose absolute value is largest.
    Side effects:  None.
    Examples:
      problem2( [9,  88, 2, -1, 5, 17, 4] )   returns 1   (index of 88)
      problem2( [9,  13, 2, -1, 5, 17, 4] )   returns 5   (index of 17)
      problem2( [9, -88, 2, -1, 5, 17, 4] )   returns 1   (index of -88)
      problem2( [-500] )                      returns 0
      problem2( [1, 2, 3, 4, 5, 6, 7, -500] ) returns 7
    Type hints:
      :type sequence [list]
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    x = sequence[0]
    for k in range(len(sequence)):
        if sequence[k] > x:
            x = sequence[k]
            index = k
        if -1*sequence[k] > x:
            x = -sequence[k]
            index = k
    return index

###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results,
                                                 format_string)


def print_actual_result_of_test(expected, actual, test_results):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise