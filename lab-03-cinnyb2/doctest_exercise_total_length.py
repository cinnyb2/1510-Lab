"""
Your name: Cindy Liu
Your student number: A01270988
"""


def total_length(first_string, second_string):
    """
    Return the sum of the lengths of first_string and second_string.

    :param first_string: a string, of course
    :param second_string: a string, of course
    :precondition: some_string is a string, possibly empty
    :precondition: second_string is a string, possibly empty
    :postcondition: correctly sums the lengths of the strings
    :return: the sum of the lengths, an integer

    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    3
    >>> total_length('YES!!!!', 'Noooooo')
    14

    #Edge case #1: Test to see if alpha numerals strings will be registed as characters.
    >>> total_length('089ujd392', 'Hello')
    14

    #Edge case #2: Test to see if different parathesis would affect function's ability to count.
    >>> total_length('Hello', "World")
    10

    #Edge case #3: Test to see if the function accepts empty strings as parameters.
    >>> total_length('', '')
    0
    """
    total_len = ''.join(first_string) + ''.join(second_string)
    return len(total_len)
