from unittest import TestCase
from unittest.mock import patch
from littlegame import generate_random_room


class TestGenerateRandomRoom(TestCase):

    @patch('random.randint', return_value=0)
    def test_generate_random_room_first_index_item(self, _):
        actual = generate_random_room()
        expected = 'You have discovered a magical room, the aura of magic fills you with wonder.'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_generate_random_room_second_index_item(self, _):
        actual = generate_random_room()
        expected = 'You have entered a room full of monster statues, you are filled with fear.'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_generate_random_room_third_index_item(self, _):
        actual = generate_random_room()
        expected = 'You have entered a room full of puppies, you are filled with happiness.'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_generate_random_room_forth_index_item(self, _):
        actual = generate_random_room()
        expected = 'You have entered an abandoned room, the nauseating stench is giving you a headache.'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_generate_random_room_last_index_item(self, _):
        actual = generate_random_room()
        expected = 'You have entered an empty room.'
        self.assertEqual(expected, actual)
