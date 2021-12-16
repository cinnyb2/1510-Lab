"""
Your name: Cindy Liu
Your student number: A01270988
"""


def average(values):
    """
    Return the average of the numbers in values.  Some items in values are
    None, and they are not counted toward the average.

    :param values: a list of numbers that may contain None
    :precondition: values is a list of numbers and/or None
    :postcondition: values is unchanged
    :return: the average of the non-None numbers in values

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0

    #Edge case #1: Test to see if average() accepts non-positive numbers such as 0 and negative numbers as parameters
    because parameters should be able to take in all types of number.
    >>> average([None, -35, -36, 0])
    -23.666666666666668

    #Edge case #2: Test to see if float numbers and integers are accepted as parameters, because parameter list
    a list of numbers.
    >>> average([20.87, 36.90, 71, 20.621784])
    37.34794599999999
    """
    copy_of_values = values
    for item in copy_of_values:
        if item is None:
            copy_of_values.remove(None)
        else:
            return sum(copy_of_values) / len(copy_of_values)

    # copy_of_values = values
    # if None in values:
    #     copy_of_values.remove(None)
    #     return sum(copy_of_values)/len(copy_of_values)
    # else:
    #     return sum(copy_of_values)/len(copy_of_values)
