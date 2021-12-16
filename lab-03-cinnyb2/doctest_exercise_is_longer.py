"""
Your name: Cindy Liu
Your student number: A01270988
"""


def is_longer(first_list, second_list):
    """'
    Return True if and only if the length of first_list
    is longer than the length of second_list.

    :param first_list: a list of course!
    :param second_list: a list of course!
    :postcondition: first_list is not changed
    :postcondition: second_list is not changed
    :return: True if first_list is longer than second_list, else False

    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    False
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
    False

    #Edge case #1: Test to see if the len() would count the whitespace as a character, and thus make first_list longer
     than second_list. If this was not a list that would be True but since len() on list only counts the string element
     both list would be equal to len of 1 and thus return False.
    >>> is_longer(['a b'], ['ab'])
    False

    #Edge case #2: Test to see if I can compare the len() of a long string to a list of numbers. If it counts the length
    of the string as single characters then it would return False but because list counts the element in the list, the
    first_list has 5 and the second_list only has 1 thus returning True.
    >>> is_longer([4, 5, 2, 3, 20], ['asdasfasfsafsafsaadfsdfs'])
    True
    """
    if len(first_list) > len(second_list):
        return True
    else:
        return False
