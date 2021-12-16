"""
Question 3 : Base conversion
"""

# Prompts user for the base they want to convert to, end base
end_base = int(input('What base are you trying to convert to (2-9)? '))

# max number user can input
max_number = ((end_base ** 4) - 1)

# tell user the max base 10 number that this program can convert to and ask for an base number
starting_base_10 = int(input('The max base 10 number this program can convert in base %s is %s. '
                             'What is your starting base 10 number? ' % (end_base, max_number)))

# # the current value, p = place
# current_value_0 = starting_base_10 // end_base
# # the remainder, n = number
# placeholder_0 = starting_base_10 % end_base


# The current value of the input base number, dividing starting base 10 number with end base
current_value = starting_base_10 // end_base
# The placeholder for the base number, using starting base 10 modulo end base
placeholder_0 = starting_base_10 % end_base


# the subsequent current value are stored in 4 different variables to make it easy for placeholder to access.
placeholder_1 = current_value % end_base
current_value = current_value // end_base

placeholder_2 = current_value % end_base
current_value = current_value // end_base

placeholder_3 = current_value % end_base
current_value = current_value // end_base

# converts it into strings so it is possible to concatenate
string_placeholder_0 = str(placeholder_0)
string_placeholder_1 = str(placeholder_1)
string_placeholder_2 = str(placeholder_2)
string_placeholder_3 = str(placeholder_3)

# reverse the order into read order
result_end_base_number = string_placeholder_3 + string_placeholder_2 + string_placeholder_1 + string_placeholder_0

print('Your number is %s in base %s. ' % (result_end_base_number, end_base))

