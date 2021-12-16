"""
Your name: Cindy Liu
Your student number: A01270988
"""


def repeat(some_string, number):
    """
    Return some_string repeated number times.

    If n is negative or zero, return an empty string.

    :param some_string: a string, of course, possibly empty
    :param number: an integer, possibly negative or zero
    :precondition: some_string is a string
    :precondition: number is an integer
    :postcondition: return a correctly multipled string
    :return: a string, possibly empty (length zero)

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'

    #Edge case #1: Test to see if it also return a string of numbers the specified number of times.
    >>> repeat('01239', 8)
    '0123901239012390123901239012390123901239'

    #Edge case #2: Test to see if repeat() take an empty string as some_string parameter. If some_string
    have no space, it should print '' regardless of the number parameter, but if there is a space between the string
    then the space should increase base on the number parameter.
    >>> repeat('', 10)
    ''
    """
    if number <= 0:
        return ''
    else:
        return some_string * number
