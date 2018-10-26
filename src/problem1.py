"""
Exam 3, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Nicolas Bohner.  October 2018.

"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


def run_test_problem1():
    """ Tests the  problem1   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')

    format_string = '    problem1( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 26
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [5, 3, 10, 8, 1, 100]
    expected = 18

    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [5, 7, 2]
    expected = 7

    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [9, 15, 12, 20, 30, 10, 8, 1, 17]
    expected = 60

    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem1(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem1(numbers):
    """
    What comes in:
      -- A non-empty sequence of numbers, with the sequence having a length
            that is evenly divisible by 3
    What goes out:
      -- Returns the sum of the middle third of the numbers in the sequence.
    Side effects:  None.
    Examples:
      problem1( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] )
                                      returns 5 + 6 + 7 + 8, which is 26

      problem1( [5, 3, 10, 8, 1, 100] )     returns 10 + 8, which is 18
      problem1( [5, 7, 2] )                              returns 7
      problem1( [9, 15, 12, 20, 30, 10, 8, 1, 17] )      returns 60
    Type hints:
      :type numbers:  [int]
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    total = 0
    for k in range(int(len(numbers)-2*(len(numbers)/3)), int(len(numbers)-(len(numbers)/3))):
        total = total+numbers[k]
    return total
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
