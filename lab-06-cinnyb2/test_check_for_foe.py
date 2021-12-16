from unittest import TestCase
from unittest.mock import patch
from littlegame import check_for_foes as check_for_foes


class TestCheckForFoe(TestCase):
    @patch('random.randint', return_value=0)
    def test_check_for_foes_foe_present(self, _):
        expected = True
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_check_for_foes_no_foes(self, _):
        expected = False
        actual = check_for_foes()
        self.assertEqual(expected, actual)



