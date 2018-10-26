"""
Exam 3, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Nicolas Bohner.  October, 2018.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def is_prime(n):
    """
    What comes in:  An integer.
    What goes out:  True if the given integer is prime, else False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    if n < 2:
        return False  # Integers less than 2 are treated as NOT prime
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above   is_prime   function - it has no TO-DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_problem3():
    """ Tests the    problem3    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3  function:')
    print('--------------------------------------------------')

    format_string = '    problem3( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [(4, 25),
                (33, 54, 20, 55, 10),
                (6, 11, 70, 33),
                (7, 11),
                (5, 5, 3)
                ]
    expected = (6, 11, 70, 33)
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [[4, 6, 8],
                [7, 10, 2]
                ]
    expected = [7, 10, 2]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [[4, 6, 8],
                [4, 6, 8]
                ]
    expected = -1
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = [[11],
                [4, 6, 8],
                [7, 10, 2]
                ]
    expected = [11]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = [[],
                []
                ]
    expected = -1
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    sequence = [[],
                [4, 6, 8],
                [10, 2, 4, 5],
                [11, 17, 53]
                ]
    expected = [10, 2, 4, 5]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    sequence = [(4, 25),
                (6, 11, 70, 33),
                (33, 54, 20, 55, 10),
                (7, 11),
                (5, 5, 3)
                ]
    expected = (6, 11, 70, 33)
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    sequence = [(4, 25),
                (6, 11, 70, 33),
                (33, 54, 20, 55, 10),
                (7, 11),
                (5, 5, 3)
                ]
    expected = (6, 11, 70, 33)
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    sequence = [(4, 25),
                (33, 54, 20, 55, 10),
                (7, 11),
                (6, 11, 70, 33),
                (5, 5, 3)
                ]
    expected = (7, 11)
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    sequence = [(4, 25),
                (33, 54, 20, 55, 10),
                (7, 11),
                (5, 5, 3),
                (6, 11, 70, 33),
                ]
    expected = (7, 11)
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    sequence = [(4, 25),
                (33, 54, 20, 55, 10),
                (7,),
                (5, 5, 3),
                (6, 11, 70, 33),
                ]
    expected = (7,)
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    sequence = [(4, 25),
                (33, 54, 20, 55, 10),
                (12, 7),
                (5, 5, 3),
                (6, 11, 70, 33),
                ]
    expected = (12, 7)
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem3(seq_of_seq):
    """
    What comes in:
      -- A sequence of sub-sequences of integers.
    What goes out:
      -- Returns the first sub-sequence that contains a number that is prime,
           or -1 if no sub-sequence contains a number that is prime.
    Side effects: None.
    Examples:
      problem3([(4, 25),
                 (33, 54, 20, 55, 10),
                 (6, 11, 70, 33),
                 (7, 11),
                 (5, 5, 3)
                ]
                returns (6, 11, 70, 33)
      problem3([[4, 6, 8], [7, 10, 2]])      returns [7, 10, 2]
      problem3([[4, 6, 8], [4, 6, 8]])       returns -1
      problem3([[4, 6, 8], [[10, 2, 4, 5]])  returns [10, 2, 4, 5]
      problem3([[], []])                     returns -1
    Type hints:
      :type seq_of_seq: list of list of int
      :rtype: (list of int) | int
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


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
