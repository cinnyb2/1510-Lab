""" This module contains 9 functions and a main function that runs two test cases for each function
    Cindy Liu
    Lab 02
    A01270988
"""
import random
import string


def triple(value):
    """

    Return triple the value.

    :param value: a rational number
    :precondition: a value must be a rational number
    :postcondition: calculate three times the value
    :return: a rational number
    """
    return value * 3


def absolute_difference(first, second):
    """
    Returns the absolute difference between two numbers.

    :param first: a rational number
    :param second: a rational number
    :precondition: a value must be a rational number
    :postcondition: calculate the correct absolute difference between two numbers
    :return: a positive int or float
    """

    return abs(first - second)


def average_of_3(first, second, third):
    """
    Return the average of three numbers.

    :param first: a rational number
    :param second: a rational number
    :param third: a rational number
    :precondition: value must be a rational number
    :postcondition: calculates the correct average between three numbers
    :return: a rational number
    """
    total = first + second + third
    return total / 3


def average_of_top_3(first, second, third, fourth):
    """
    Return the average of the top 3 numbers.

    :param first: a rational number
    :param second: a rational number
    :param third: a rational number
    :param fourth: a rational number
    :precondition: value must be a rational number
    :postcondition: calculates the average of the top three numbers
    :return: a rational number
    """
    smallest_number = min(first, second, third, fourth)
    total = ((first + second + third + fourth) - smallest_number)
    return total / 3


def base_convert(base_10_number, destination_base):
    """
    Return the first two digits representing the destination base when given a base 10 number.

    :param base_10_number: an int
    :param destination_base: an int
    :precondition: value must be a positive integer and cannot be longer than the two digits destination number
    :postcondition: converts base 10 number into 2 digit representation of destination base
    :return: an int
    """
    # divide the base 10 number by destination and get remainder
    current_value = base_10_number // destination_base
    remainder_0 = base_10_number % destination_base

    remainder_1 = current_value % destination_base
    # current_value = current_value // destination_base

    current_value = str(remainder_1) + str(remainder_0)

    return current_value


def name(length):
    """
    Return a string of random letter in the length specified with the first letter capitalized.

    :param length: a positive integer
    :precondition: value must be positive integer
    :postcondition: returns a string of random letter of the length specified with the first letter capitalized
    :return: a str
    """
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    return random_string.capitalize()


def celsius_to_target(celsius_unit, target_scale):
    """
    Convert from celsius temperature unit to target temperature unit.

    Return the number representation of target scale that has been converted from celsius
    :param celsius_unit: a float
    :param target_scale: a str
    :precondition: value must a float, and one of the temperature scale listed
    :postcondition: converts from celsius unit to target scale
    :return: a float
    """

    if target_scale == 'Kelvin':
        return celsius_unit + 273.15
    if target_scale == 'Celsius':
        return celsius_unit
    if target_scale == 'Fahrenheit':
        return celsius_unit * 9/5 + 32
    if target_scale == 'Rankine':
        return (celsius_unit + 273.15) * 9/5
    if target_scale == 'Romer':
        return celsius_unit * 21/40 + 7.5
    if target_scale == 'Newton':
        return celsius_unit * 33/100
    if target_scale == 'Delisle':
        return (100 - celsius_unit) * 3/2
    if target_scale == 'Reaumur':
        return celsius_unit * 4/5


def base_to_celsius(base_scale, celsius_unit):
    """
    Converts the base temperature scale into celsius temperature unit.

    :param celsius_unit: a float
    :param base_scale: a str
    :precondition: value must a float, and one of the temperature scale listed
    :postcondition: convert from base scale to celsius unit
    :return: a float
    """
    if base_scale == 'Kelvin':
        return celsius_unit - 273.15
    if base_scale == 'Celsius':
        return celsius_unit
    if base_scale == 'Fahrenheit':
        return (celsius_unit - 32) * 5/9
    if base_scale == 'Rankine':
        return (celsius_unit - 491.67) * 5/9
    if base_scale == 'Romer':
        return (celsius_unit - 7.5) * 40/21
    if base_scale == 'Newton':
        return celsius_unit * 100/33
    if base_scale == 'Delisle':
        return (100 - celsius_unit) * 2/3
    if base_scale == 'Reaumur':
        return celsius_unit * 5/4


def convert_temperature(source_units, source_scale, target_scale):
    """
    Convert from source temperature scale to target temperature scale.

    :param source_units: a float
    :param source_scale: a str
    :param target_scale: a str
    :precondition: value must a float, and one of the temperature scale listed.
    The temperature scale must be a string and it must be spelled correctly starting
    with a capital
    :postcondition: return the target temperature number from source temperature scale
    :return: a float
    """
    converted_temperature = celsius_to_target(base_to_celsius(source_scale, source_units), target_scale)
    return converted_temperature


def main():
    """
    Drive the program.

    """
    print(triple(3.6))
    print(triple(-8))

    print(absolute_difference(3, 7/3))
    print(absolute_difference(-64, 64))

    print(average_of_3(4, -6, 9))
    print(average_of_3(122, 236, 987))

    print(average_of_top_3(4, 7, -9, -9.5))
    print(average_of_top_3(28, 36, 21, 57))

    print(base_convert(2, 10))
    print(base_convert(16, 9))

    print(name(12))
    print(name(5))

    print(convert_temperature(-218.52, 'Reaumur', 'Fahrenheit'))
    print(convert_temperature(160, 'Celsius', 'Celsius'))


if __name__ == "__main__":
    main()
