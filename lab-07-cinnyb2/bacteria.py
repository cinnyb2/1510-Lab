import sys


def colonize(surface_width: int, surface_height: int, x_start: int, y_start: int, generation: int) -> None:
    """
    Create a colony of bacteria on a surface.

    :param generation: integer, can be 0
    :param surface_width: a positive integer
    :param surface_height:  a positive integer
    :param x_start: a positive integer
    :param y_start: a positive integer
    :precondition: generation cannot be negative
    :precondition: width and height must be positive integers
    :precondition: x and y coordinates must be >= width and height of the surface
    :postcondition: creates a colony of bacteria on a surface
    :return: None
    """
    surface = {(height, width): False for height in range(surface_height) for width in range(surface_width)}
    spread_like_bacteria(surface, x_start, y_start, generation)
    print_surface(surface, surface_width, surface_height)


def spread_like_bacteria(surface: dict, x_start: int, y_start: int, max_generation: int) -> None:
    """
    Spread the bacteria recursively if location is valid.

    :param max_generation: integer, can be 0
    :param y_start: a positive integer
    :param x_start: a positive integer
    :param surface: a positive integer
    :precondition: max_generation cannot be negative
    :precondition: if generation is 0 then the function will stop spreading
    :postcondition: spread the bacteria recursively in 4 directions (down, up, right, left)
    :return: None
    """
    # base case, check to see if you can populate an valid location
    if valid_location(surface, x_start, y_start):
        surface.update({(x_start, y_start): True})
        max_generation -= 1  # decrease the generation so that there is no infinite loop

        if max_generation >= 0:
            # recursively spread based if there is >= 0 generation
            spread_like_bacteria(surface, x_start - 1, y_start, max_generation)  # down
            spread_like_bacteria(surface, x_start + 1, y_start, max_generation)  # top
            spread_like_bacteria(surface, x_start, y_start + 1, max_generation)  # right
            spread_like_bacteria(surface, x_start, y_start - 1, max_generation)  # left


def print_surface(surface: dict, width: int, height: int) -> None:
    """
    Print the surface of the bacterial colony.

    * is the start point and 0 is all the area not infected by the bacteria

    :param surface: dictionary with all the coordinate tuples
    :param width: a positive integer
    :param height: a positive integer
    :precondition: width and height must be positive integers
    :precondition: x and y coordinates must be >= width and height of the surface
    :postcondition: prints the surface of the bacterial colony
    :return: None
    """
    for row in range(height):
        for column in range(width):
            if surface[(column, row)]:
                print('*', end="")
            else:
                print('0', end="")
        print()  # adds a new line, so it prints correctly


def valid_location(surface: dict, x_start: int, y_start: int) -> bool:
    """
    Check to see if the location is valid for the bacteria to infect.

    :param surface: dictionary with all the coordinate tuples
    :param x_start: a positive integer
    :param y_start: a positive integer
    :precondition: the x and y_start must be be positive integers
    :postcondition: prints the surface of the bacterial colony
    :return: True or False
    """
    # Checks to see if coordinate tuple is in surface dict keys and their value is false
    if (x_start, y_start) in surface.keys() and surface[(x_start, y_start)] is False:
        return True
    else:
        return False


def main():
    # sys.argv returns a list, with each of the index referring to the param
    colonize(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))


if __name__ == "__main__":
    main()
