from unittest import TestCase
from littlegame import check_if_goal_attained as goal_achieved


class TestCheckIfGoalAttained(TestCase):
    def test_check_if_goal_attained_goal_not_achieved(self):
        board = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (1, 2): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (2, 0): 'You have entered an empty room.',
                 (2, 1): 'You have entered an empty room.',
                 (2, 2): 'You have entered an empty room.',
                 (3, 0): 'You have entered an empty room.',
                 (3, 1): 'You have entered an empty room.',
                 (3, 2): 'You have entered an empty room.',
                 (3, 3): 'You have entered an empty room.'}
        character = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 5}
        expected = False
        actual = goal_achieved(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_goal_achieved(self):
        board = {(0, 0): 'You have discovered a magical room, the aura of magic fills you with wonder.',
                 (0, 1): 'You have entered a room full of monster statues, you are filled with fear.',
                 (1, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (1, 1): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (1, 2): 'You have entered an abandoned room, the nauseating stench is giving you a headache.',
                 (2, 0): 'You have entered an empty room.',
                 (2, 1): 'You have entered an empty room.',
                 (2, 2): 'You have entered an empty room.',
                 (3, 0): 'You have entered a room full of puppies, you are filled with happiness.',
                 (3, 1): 'You have entered an empty room.',
                 (3, 2): 'You have entered an empty room.',
                 (3, 3): 'You have entered an empty room.'}
        character = {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 5}
        expected = True
        actual = goal_achieved(board, character)
        self.assertEqual(expected, actual)
