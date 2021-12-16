"""
Your name: Cindy Liu
Your student number: A01270988
"""


def same_first_last(a_list):
    """
    Return True if and only if first item of the list
    is the same as the last item in the list.

    :param a_list: a list of course!
    :precondition: len(a_list) >= 2
    :postcondition: return true if the first/last elements are the same
    :postcondition: a_list is unchanged
    :return: True if the first/last elements are the same, else False

    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0, 4.5])
    False

    #Edge case #1: Test to see if all the items in the list are the same character would have an impact on what is
    return.
    >>> same_first_last(['Axel', 'Axel', 'Axel', 'Axel'])
    True

    #Edge case #2: Test to see if an added whitespace on the last number in the list would return False despite it
    being the same number as the first number.
    >>> same_first_last([2, 3, 4, 6, 8, 9, 1, 2 ])
    True
    """
    if a_list[0] == a_list[-1]:
        return True
    else:
        return False
