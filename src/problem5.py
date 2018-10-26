"""
Final exam, problem 2.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Nicolas Bohner.  May 2018.

"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem5()


def is_prime(n):
    """
    What comes in:  An integer n.
    What goes out:
      -- Returns True if the given integer is prime,
                 False if the given integer is NOT prime.
         Treats integers less than 2 as NOT prime.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
      -- is_prime(1)  returns  False
    Note: The algorithm used here is simple and clear but slow.
    """
    if n < 2:
        return False
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


def run_test_problem5():
    """ Tests the  problem5   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem5   function:')
    print('--------------------------------------------------')

    format_string = '    problem5( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    x = 17
    expected = 23
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    x = 101
    expected = 101
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    x = 4
    expected = 5
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    x = 61
    expected = 61
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    x = 62
    expected = 67
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    x = 9999
    expected = 10037
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    x = 5555555
    expected = 5555629
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    x = 10000001
    expected = 10000019
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    x = 111
    expected = 113
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    x = 112
    expected = 113
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    x = 113
    expected = 113
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    x = 114
    expected = 131
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem5(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)
    
    
def problem5(x):
    """
    What comes in:  An integer  x  that is at least 2.
    What goes out:
      -- Returns the smallest prime such that:
           -- the prime is bigger than or equal to x, AND
           -- the (sum of the digits of the prime) is itself prime.
    Side effects:  None.
    Examples:
      problem5( 17)   returns  23  because:
            - the sum of the digits of 17 is 8, which is NOT prime
            - 18 is not prime
            - the sum of the digits of 19 is 10, which is NOT prime
            - 20 is not prime
            - 21 is not prime
            - 22 is not prime
            - the sum of the digits of 23 is 5, which IS prime
      problem5( 101 )    returns 101  (because 101 and 1 + 0 + 1 = 2 are prime)
      problem5(   4 )    returns 5
      problem5(  61 )    returns 61
      problem5(  62 )    returns 67
    Type hints:
      :type x:    int
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    while True:
        if is_prime(x)is True:
            if is_prime(sum_of_digits(x)) is True:
                return x
        x = x+1


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