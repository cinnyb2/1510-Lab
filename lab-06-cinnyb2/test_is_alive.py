from unittest import TestCase
from littlegame import is_alive as is_alive


class TestIsAlive(TestCase):
    def test_character_is_alive(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        expected = True
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_character_is_dead(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 0}
        expected = False
        actual = is_alive(character)
        self.assertEqual(expected, actual)
