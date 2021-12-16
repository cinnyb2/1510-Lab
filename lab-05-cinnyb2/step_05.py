"""
Step 05.
How do we watch a variable?
"""


def sorted_merge_list(list_one: list, list_two: list) -> list:
    """
    Returns an alphabetically sorted merged list that contain all the elements of two lists.

    :param list_one: a list of strings, can also be empty
    :param list_two: a list of strings, can also be empty
    :precondition: both lists must have the same length, and the alphabets string in each list must either be upper or
    lower case not a mix. The two list argument must only contain strings alphabets (no numbers or special characters),
    and already be sorted in alphabetical order. The list with the higher letter order must be put into list_one (e.g.
    J is higher than A).
    :postcondition: correctly returns an alphabetically sorted merged list of strings that contains all
    the elements of two list
    :return: a list of strings, can also be empty

    >>> names_from_a_to_h = ['Amy', 'Bob', 'Chloe', 'David', 'Emerald', 'Frances', 'George', 'Hertie']
    >>> names_starting_with_j = ['Jacky', 'Jae', 'James', 'Janelle', 'Jasmine', 'Jason', 'Jolene', 'Joseph']
    >>> sorted_merge_list(names_starting_with_j, names_from_a_to_h)
    ['Amy', 'Bob', 'Chloe', 'David', 'Emerald', 'Frances', 'George', 'Hertie', 'Jacky', 'Jae', 'James', 'Janelle', \
'Jasmine', 'Jason', 'Jolene', 'Joseph']

    >>> month_1 = ['march', 'april']
    >>> month_2 = ['January', 'February']
    >>> sorted_merge_list(month_1, month_2)
    ['January', 'February', 'march', 'april']

    """

    result = []
    index_of_list_1 = 0
    index_of_list_2 = 0
    while index_of_list_1 != len(list_one) or index_of_list_2 != len(list_two):
        if index_of_list_2 == len(list_two) and index_of_list_1 != len(list_one) or list_one[index_of_list_1] <= \
                list_two[index_of_list_2]:
            result.append(list_one[index_of_list_1])
            index_of_list_1 += 1
        else:
            result.append(list_two[index_of_list_2])
            index_of_list_2 += 1

    return result


# result_list = []
    # index_of_list_1 = 0
    # index_of_list_2 = 0
    # while index_of_list_1 != len(list_one) and index_of_list_2 != len(list_two):
    #     if index_of_list_1 <= index_of_list_2:
    #         result_list.append(list_one[index_of_list_1])
    #         index_of_list_1 += 1
    #     if index_of_list_2 <= index_of_list_1:
    #         result_list.append(list_two[index_of_list_2])
    #         index_of_list_2 += 1
    #
    # for item in range(len(result_list)):
    #     for char in range(len(result_list)-1):
    #         if result_list[char] > result_list[char + 1]:
    #             result_list[char], result_list[char + 1] = result_list[char + 1], result_list[char]
    # return result_list


def main():
    names_from_a_to_h = ['Amy', 'Bob', 'Chloe', 'David', 'Emerald', 'Frances', 'George', 'Hertie']
    names_starting_with_j = ['Jacky', 'Jae', 'James', 'Janelle', 'Jasmine', 'Jason', 'Jolene', 'Joseph']
    all_the_names = sorted_merge_list(names_starting_with_j, names_from_a_to_h)
    print(all_the_names)


if __name__ == '__main__':
    main()
