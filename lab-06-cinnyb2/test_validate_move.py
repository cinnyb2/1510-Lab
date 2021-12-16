from unittest import TestCase
from littlegame import validate_move as validate_move


class TestValidateMove(TestCase):
    def test_validate_move_valid_direction(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        board = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (1, 2): 'You have entered an empty room.',
                 (2, 0): 'You have entered an empty room.',
                 (2, 1): 'You have entered an empty room.',
                 (2, 2): 'You have entered an empty room.',
                 (3, 0): 'You have entered an empty room.',
                 (3, 1): 'You have entered an empty room.',
                 (3, 2): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (3, 3): 'You have entered an empty room.'}
        direction = 'North'
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_direction(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        board = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (1, 2): 'You have entered an empty room.',
                 (2, 0): 'You have entered an empty room.',
                 (2, 1): 'You have entered an empty room.',
                 (2, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 0): 'You have entered an empty room.',
                 (3, 1): 'You have entered an empty room.',
                 (3, 2): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (3, 3): 'You have entered an empty room.'}
        direction = 'West'
        actual = validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)
