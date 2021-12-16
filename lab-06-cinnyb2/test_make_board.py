from unittest import TestCase
from unittest.mock import patch
from littlegame import make_board


class TestMakeBoard(TestCase):
    @patch('random.randint', return_value=1)
    def test_make_board_2_by_2_even_rectangle_with_only_one_type_of_room(self, _):
        rows = 2
        columns = 2
        actual = make_board(rows, columns)
        expected = {(0, 0): 'You have entered a room full of monster statues, you are filled with fear.',
                    (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                    (1, 0): 'You have entered a room full of monster statues, you are filled with fear.',
                    (1, 1): 'You have entered a room full of monster statues, you are filled with fear.'}
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[0, 1, 2, 3, 4])
    def test_make_board_2_by_2_even_rectangle_with__s(self, _):
        rows = 2
        columns = 2
        actual = make_board(rows, columns)
        expected = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                    (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                    (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                    (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.'}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_even_make_board_with_more_columns_than_rows(self, _):
        rows = 3
        columns = 4
        actual = make_board(rows, columns)
        expected = {(0, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                    (0, 1): 'You have entered a room full of puppies, you are filled with happiness.',
                    (0, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                    (0, 3): 'You have entered a room full of puppies, you are filled with happiness.',
                    (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                    (1, 1): 'You have entered a room full of puppies, you are filled with happiness.',
                    (1, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                    (1, 3): 'You have entered a room full of puppies, you are filled with happiness.',
                    (2, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                    (2, 1): 'You have entered a room full of puppies, you are filled with happiness.',
                    (2, 2): 'You have entered a room full of puppies, you are filled with happiness.',
                    (2, 3): 'You have entered a room full of puppies, you are filled with happiness.'}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_uneven_make_board_with_more_rows_than_columns(self, _):
        rows = 4
        columns = 3
        actual = make_board(rows, columns)
        expected = {(0, 0): 'You have entered an empty room.',
                    (0, 1): 'You have entered an empty room.',
                    (0, 2): 'You have entered an empty room.',
                    (1, 0): 'You have entered an empty room.',
                    (1, 1): 'You have entered an empty room.',
                    (1, 2): 'You have entered an empty room.',
                    (2, 0): 'You have entered an empty room.',
                    (2, 1): 'You have entered an empty room.',
                    (2, 2): 'You have entered an empty room.',
                    (3, 0): 'You have entered an empty room.',
                    (3, 1): 'You have entered an empty room.',
                    (3, 2): 'You have entered an empty room.'}
        self.assertEqual(expected, actual)
