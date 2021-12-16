"""
Your name: Cindy Liu
Your student number: A01270988
"""
import doctest


def sparse_add(vector_one, vector_two):
    """

    Return the sum of two vectors as the element-wise sum of their elements in a dictionary of non-zero entries.

    The index is the key and the entry is the value. Length will also be included in the dictionary.

    :param vector_one: dictionary of vectors
    :param vector_two: dictionary of vectors
    :precondition: two vector argument must be given and both vectors have to be the same lengths, entries must be
    integers. The length cannot be negative.
    :postcondition: returns the correct addition between two vectors and the length, only the non-zero elements will
    added to the dictionary. The vector cannot be empty, so the length cannot be 0.
    :return: dictionary of factors

    >>> sparse_add({'length': 3, 0: 1, 2: 3} ,{'length': 3, 0: 4, 1: 5, 2: 6})
    {'length': 3, 0: 5, 2: 9, 1: 5}

    >>> sparse_add({'length': 36, 7: -9} ,{1: -6, 'length': 36})
    {'length': 36, 7: -9, 1: -6}
    """
    copy_two = vector_two.copy()
    copy_two.pop("length", None)

    merged = vector_one.copy()
    for key, value in copy_two.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value

    for key in merged.copy():
        if merged[key] == 0:
            del merged[key]
    return merged

    # 2nd way longer and not as elegant
    # vector_two_unique_keys = copy_two.keys() - vector_one.keys()
    # vector_one_unique_keys = vector_one.keys() - copy_two.keys()
    # common_keys = copy_two.keys() & vector_one.keys()
    # sum_dict = {}
    #
    # for item in common_keys:
    #     sum_dict[item] = vector_one[item] + copy_two[item]
    # for item in vector_two_unique_keys:
    #     sum_dict[item] = copy_two[item]
    # for item in vector_one_unique_keys:
    #     sum_dict[item] = vector_one[item]
    #
    # return sum_dict

    # 3rd way that sort the dictionary ( will give double the length)
    # merged = dict()
    # vector_one_keys = list(vector_one.keys())
    # vector_two_keys = list(vector_two.keys())
    #
    # # merge values by key size
    # i, j = 0, 0
    # while i < len(vector_one_keys) and j < len(vector_two_keys):
    #     if vector_one_keys[i] < vector_two_keys[j]:
    #         merged[vector_one_keys[i]] = vector_one[vector_one_keys[i]]
    #         i += 1
    #     elif vector_one_keys[i] > vector_two_keys[j]:
    #         merged[vector_two_keys[j]] = vector_two[vector_two_keys[j]]
    #         j += 1
    #     else:
    #         merged[vector_one_keys[i]] = vector_one[vector_one_keys[i]] + vector_two[vector_two_keys[j]]
    #         i += 1
    #         j += 1
    #
    # # vector one has values we haven't merged yet
    # while i < len(vector_one_keys):
    #     merged[vector_one_keys[i]] = vector_one[vector_one_keys[i]]
    #     i += 1
    #
    # # vector two has values we haven't merged yet
    # while j < len(vector_two_keys):
    #     merged[vector_two_keys[j]] = vector_two[vector_two_keys[j]]
    #     j += 1
    #
    # return merged


def sparse_dot_product(vector_one, vector_two):
    """

    Return the sum of two vectors as the element-wise product of their elements in a dictionary of non-zero
    entries.

    The index is the key and the entry is the value. Length will also be included in the dictionary.

    :param vector_one: dictionary of vectors
    :param vector_two: dictionary of vectors
    :precondition: two vector argument must be given and both vectors have to be the same lengths, entries must be
    integers. The length cannot be negative.
    :postcondition: returns the correct multiplication of the vectors and the length, only the non-zero elements will
    added to the dictionary. The vector cannot be empty, so the length cannot be 0.
    :return: int

    >>> sparse_dot_product({'length': 3, 0: 1, 2: 3} ,{'length': 3, 0: 4, 1: 5, 2: 6})
    22
    >>> sparse_dot_product({'length': 36, 7: -9} ,{1: -6, 'length': 36})
    0
    >>> sparse_dot_product({1: -6, 2: 4, 'length': 300}, {'length': 300, 1: 1, 2: -2})
    -14
    """
    vector_one_copy = vector_one.copy()
    vector_two_copy = vector_two.copy()
    vector_two_copy.pop("length", None)
    vector_one_copy.pop("length", None)

    result = 0
    for key, value in vector_one_copy.items():
        if key in vector_two_copy:
            result += vector_two_copy[key] * value
    return result


def main():
    """
    Drives the function
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
