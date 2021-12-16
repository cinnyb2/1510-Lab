"""
Step 02.
Step into and over function calls.
"""


def convert_to_upper_case(message):
    converted_message = message.upper()
    return converted_message


def display_urgent_message(message):
    urgent_message = convert_to_upper_case(message)
    print(urgent_message)


def main():
    """
    Drive the program.
    """
    message = "This is a debugging tutorial"
    display_urgent_message(message)


if __name__ == "__main__":
    main()
