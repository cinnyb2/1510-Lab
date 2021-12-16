"""
Step 03.
Create a conditional breakpoint.
"""

import sys


def main(upper_bound):
    """
    Drive the program.
    """
    some_variable = 1
    for integer in range(1, upper_bound):
        some_variable *= integer
    print(f"The final value is {some_variable}")


if __name__ == "__main__":
    main(int(sys.argv[1]))
