import io
from unittest import TestCase
from littlegame import move_character as move
from unittest.mock import patch


class TestMoveCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_west_from_end(self, _):
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
                 (3, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 3): 'You have entered an empty room.'}
        character = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 5}
        direction = 'West'
        actual = move(board, character, direction)
        expected = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5}
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_north_from_start(self, _):
        board = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (1, 2): 'You have entered an empty room.',
                 (2, 0): 'You have entered a room full of monster statues, you are filled with fear.',
                 (2, 1): 'You have entered an empty room.',
                 (2, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 0): 'You have entered an empty room.',
                 (3, 1): 'You have entered an empty room.',
                 (3, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 3): 'You have entered an empty room.'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = 'North'
        actual = move(board, character, direction)
        expected = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_east_from_middle_of_the_board(self, _):
        board = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (1, 2): 'You have entered an empty room.',
                 (2, 0): 'You have entered a room full of monster statues, you are filled with fear.',
                 (2, 1): 'You have entered an empty room.',
                 (2, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (3, 1): 'You have entered an empty room.',
                 (3, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 3): 'You have entered an empty room.'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 'East'
        actual = move(board, character, direction)
        expected = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_south(self, _):
        board = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (1, 2): 'You have entered an empty room.',
                 (2, 0): 'You have entered a room full of monster statues, you are filled with fear.',
                 (2, 1): 'You have entered an empty room.',
                 (2, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (3, 1): 'You have entered an empty room.',
                 (3, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 3): 'You have entered a room full of puppies, you are filled with happiness.'}
        character = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
        direction = 'South'
        actual = move(board, character, direction)
        expected = {'X-coordinate': 2, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_out_of_bounds(self, _):
        board = {(0, 0): 'You have entered an empty room.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (1, 2): 'You have entered an empty room.',
                 (2, 0): 'You have entered a room full of monster statues, you are filled with fear.',
                 (2, 1): 'You have entered an empty room.',
                 (2, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (3, 1): 'You have entered an empty room.',
                 (3, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 3): 'You have entered a room full of puppies, you are filled with happiness.'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = 'West'
        actual = move(board, character, direction)
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(actual, expected)
