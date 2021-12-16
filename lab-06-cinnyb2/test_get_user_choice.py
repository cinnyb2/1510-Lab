import io
from unittest import TestCase
from littlegame import get_user_choice as choice
from unittest.mock import patch


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['S'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_string_letter_uppercase(self, _, __):
        expected_output = 'South'
        actual_output = choice()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_string_int(self, _, __):
        expected_output = 'North'
        actual_output = choice()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['e'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_string_lowercase(self, _, __):
        expected_output = 'East'
        actual_output = choice()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['West'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_string_full_letter_title_case(self, _, __):
        expected_output = 'West'
        actual_output = choice()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['west'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_string_full_letter_lower_case(self, _, __):
        expected_output = 'West'
        actual_output = choice()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['Ehf4839t', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_incorrect_input(self, mock_output, _):
        expected_return = choice()
        actual = mock_output.getvalue()
        expected = "That is an invalid answer. Please try again: \n"
        self.assertTrue(expected in actual)
        self.assertEqual('East', expected_return)

    @patch('builtins.input', side_effect=['Wes', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_input_incorrect_input_similar_to_keyword(self, mock_output, _):
        expected_return = choice()
        actual = mock_output.getvalue()
        expected = "That is an invalid answer. Please try again: \n"
        self.assertTrue(expected in actual)
        self.assertEqual('West', expected_return)


