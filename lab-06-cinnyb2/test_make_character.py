from unittest import TestCase
from littlegame import make_character as character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        actual = character()
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(expected, actual)
