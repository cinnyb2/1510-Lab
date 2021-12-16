"""
A little game.
"""
import random


def generate_random_room():
    """
    Returns a random room description out of a list of random room descriptions.

    :precondition: the random room description index has to be one of the 5 room description in the list specified (0,4)
    :postcondition: correctly returns a random room description out of a list of room descriptions
    @return: a string describing the room
    """
    random_room = ['You have discovered a magical room, the aura of magic fills you with wonder.',
                   'You have entered a room full of monster statues, you are filled with fear.',
                   'You have entered a room full of puppies, you are filled with happiness.',
                   'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                   'You have entered an empty room.']

    return random_room[random.randint(0, 4)]


def make_board(rows, columns):
    """
    Creates a game board dictionary the size of the rows and column argument.

    The dictionary format will be {(x, y): 'room description'}, where the x and y coordinates tuple will be the keys and
    the value will be a random room description.

    @param rows: positive non-zero integer
    @param columns: positive non-zero integer
    :precondition: both rows and columns must be positive non-zero integer
    :precondition: param must be >= 2
    :postcondition: correctly returns a dictionary
    @return: a dictionary
    """

    dict_board = {(row, column): generate_random_room() for row in range(rows) for column in range(columns)}
    return dict_board


def make_character():
    """
    Creates a character dictionary that contains their position on the game board and their current HP.

    :precondition: each character starts at the x and y position (0, 0) and have 5 HP
    :postcondition: creates a character dictionary that contains their position on the game board and their current HP
    @return: dictionary with character information

    >>> player = make_character()
    >>> player
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    character_dict = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    return character_dict


def describe_current_location(board, character):
    """
    Describe the room description and the current board coordinates of the character.

    @param board: a dictionary
    @param character: a dictionary
    :precondition: character must be within the playing boundary of the board, and the exact coordinates of the
    character must be present in the board
    :precondition: character's HP must > 0
    :precondition: board must be unchanged
    :postcondition: describe the room description and the current board coordinates of the character
    @return: None

    >>> player = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> describe_current_location(board_map, player)
    room 3 (1, 2)

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> describe_current_location(board_map, player)
    room 1 (0, 0)
    """

    coordinates_tuple = (character['X-coordinate'], character['Y-coordinate'])
    description = board[coordinates_tuple]

    print(description, coordinates_tuple)


def get_user_choice():
    """
    Prompt the user to enter which direction they wish to go.

    :precondition: user must input either the number, the starting letter or full direction corresponding to the
    direction they wish to go for input to register (e.g. '1', 'n', 'north', or 'North')
    :postcondition: user will enter the direction they wish to go
    @return: string stating direction 'North', 'East', 'South', 'West'
    """
    print('1. North \n' 
          '2. East \n'
          '3. South \n'
          '4. West \n'
          'Please enter the number that corresponds to the direction you want to go '
          '(1, 2, 3, 4): ')
    user_direction_input = input()

    user_direction_input = user_direction_input.lower()

    choice_dict = {'North': ['1', 'n', 'north'], 'East': ['2', 'e', 'east'],
                   'South': ['3', 's', 'south'], 'West': ['4', 'w', 'west']}

    while True:
        for key, values in choice_dict.items():
            if user_direction_input in values:
                return key

        print("That is an invalid answer. Please try again: ")
        user_direction_input = input()


def validate_move(board, character, direction):
    """
    Validate whether the character is on the board and whether they can travel on to their desired direction on the map

    @param board: a dictionary
    @param character: a dictionary
    @param direction: a string from ['North', 'East', 'South', 'West']
    :precondition: the new position that the characcter moves to must be on the board
    :precondition: board must be unchanged
    :postcondition: validate correctly whether the character is on the board and whether they can travel on to their
    desired direction on the map
    @return: True or False


    >>> player = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> path = 'North'
    >>> validate_move(board_map, player, path)
    True

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> path = 'West'
    >>> validate_move(board_map, player, path)
    False
    """
    x_value = character['X-coordinate']
    y_value = character['Y-coordinate']

    if direction == 'North':
        y_value += 1
    elif direction == 'East':
        x_value += 1
    elif direction == 'South':
        y_value -= 1
    elif direction == 'West':
        x_value -= 1
    else:
        return False  # invalid direction

    return (x_value, y_value) in board.keys()


def move_character(board, character, direction):
    """

    Move the character to the character to their new location given direction.

    @param board: dictionary of board coordinates with corresponding room description
    @param character: dictionary of character's coordinates and HP
    @param direction: a string from ['North', 'East', 'South', 'West']
    :precondition: direction must be one either North, East, South or West
    :precondition: board must be unchanged
    :precondition: the move must be validate (both the current position and the new position must be present on the
    board)
    :postcondition: move the character to the character to their new location given direction
    @return: dictionary of character's new coordinates

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4', (1, 1): 'random 5'}
    >>> path = 'East'
    >>> move_character(board_map, player, path)
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    """

    if validate_move(board, character, direction):
        if direction == 'North':
            character['Y-coordinate'] += 1
        elif direction == 'East':
            character['X-coordinate'] += 1
        elif direction == 'South':
            character['Y-coordinate'] -= 1
        elif direction == 'West':
            character['X-coordinate'] -= 1
    return character


def check_for_foes():
    """
    Returns True or False based on whether you have encountered a foe.

    :precondition: chance of encountering foe is always 25% and cannot be changed
    :postcondition: returns True or False based on whether you have encountered a foe
    @return: True or False
    """
    return random.randint(0, 3) < 1


def guessing_game(character):
    """
    Prompt user to play a guessing game.

    Users have to input a number from 1 to 5, if they do not answer the correct number they will receive 1 HP of damage.

    :@param character: dictionary of character's coordinates and HP
    :precondition: character HP > 1 before starting the guessing game
    :precondition: the user must enter a number in range(1, 6), any other number will be wrong and damage will be
    inflicted on the character
    :postcondition: Users have to input a number from 1 to 5, if they do not answer the correct number they will receive
    1 HP of damage
    @return: None
    """
    user_guess = int(input('You have encountered an enemy! Pick a number from 1 to 5: '))
    secret_number = random.randint(1, 5)
    if user_guess == secret_number:
        print(f'You\'ve guessed right!, the number was {secret_number}.')
    else:
        character['Current HP'] -= 1
        hp = character['Current HP']
        print(f'Sorry, that was not the number. I am going to have to hurt you. Your HP is now {hp}.')


def check_if_goal_attained(board, character):
    """
    Check to see if the character has reached the destination (3, 3).

    True if character has reached destination else False.

    @param board: dictionary
    @param character: dictionary
    :precondition: character must be within the board boundary
    :precondition: board must be unchanged
    :postcondition: check to see if the character has reached the destination (3, 3)
    @return: True or False
    >>> player = {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (3, 3): 'room 3'}
    >>> check_if_goal_attained(board_map, player)
    True

    >>> player = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
    >>> board_map = {(0, 0): 'room 1', (1, 0): 'room 2', (1, 2): 'room 3', (1, 3): 'room 4'}
    >>> check_if_goal_attained(board_map, player)
    False
    """
    coordinates_tuple = (character['X-coordinate'], character['Y-coordinate'])
    if coordinates_tuple == (3, 3) in board.keys():
        return True
    else:
        return False


def is_alive(character):
    """

    Return whether or not the character is still alive.

    @param character: dictionary with character's information (x, y coordinates, and current HP)
    :precondition: character cannot have < 0 HP
    :postcondition: Return whether or not the character is still alive
    @return: True or False

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> is_alive(player)
    True

    >>> player = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 0}
    >>> is_alive(player)
    False
    """
    return False if character['Current HP'] == 0 else True


def game():
    """
    Drive the entire game.
    """
    rows = 4
    columns = 4
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        # Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(board, character, direction)
            # describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)
            achieved_goal = check_if_goal_attained(board, character)
        else:
            print("Oh no, you have reached the a dead end!")

    if achieved_goal:
        print("Congratulations you have finished the game!")
    if not is_alive(character):
        print("You died a brave soul.")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
