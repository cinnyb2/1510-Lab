import io
from unittest import TestCase
from littlegame import guessing_game as guessing_game
from unittest.mock import patch


class TestGuessingGame(TestCase):
    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guessed_correctly(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'You\'ve guessed right!, the number was 1.\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 2, 4, 5])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guessed_incorrectly_with_full_health(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Sorry, that was not the number. I am going to have to hurt you. Your HP is now 4.\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 2, 4, 5])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guessed_incorrectly_with_3_HP(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 3}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Sorry, that was not the number. I am going to have to hurt you. Your HP is now 2.\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 3, 4, 5])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guessed_incorrectly_with_2HP(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 2}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Sorry, that was not the number. I am going to have to hurt you. Your HP is now 1.\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5])
    @patch('random.randint', return_value=9)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guessed_incorrect_number_out_of_range(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Sorry, that was not the number. I am going to have to hurt you. Your HP is now 4.\n'
        self.assertEqual(expected_output, the_game_printed_this)
