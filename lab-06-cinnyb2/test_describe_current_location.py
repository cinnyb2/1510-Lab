import io
from unittest import TestCase
from unittest.mock import patch
from littlegame import describe_current_location as describe_location


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_start_position(self, mock_output):
        board = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        expected = 'You have discovered a magical room, the aura of magic fills you with wonder. (0, 0)\n'
        describe_location(board, character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_almost_end_position(self, mock_output):
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
                 (3, 2): 'You have entered an empty room.',
                 (3, 3): 'You have entered an empty room.'}
        character = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 5}
        expected = 'You have entered an empty room. (3, 2)\n'
        describe_location(board, character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
