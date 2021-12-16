from unittest import TestCase
from step_05 import sorted_merge_list as merge


class TestSortedMergeList(TestCase):
    def test_sorted_merge_list_empty_list(self):
        list_one = []
        list_two = []
        expected = []
        actual = merge(list_one, list_two)
        self.assertEqual(expected, actual)

    def test_sorted_merge_list_of_single_element_uppercase(self):
        list_one = ['Hello']
        list_two = ['Chris']
        expected = ['Chris', 'Hello']
        actual = merge(list_one, list_two)
        self.assertEqual(expected, actual)

    def test_sorted_merge_list_of_single_element_lowercase(self):
        list_one = ['hello']
        list_two = ['chris']
        expected = ['chris', 'hello']
        actual = merge(list_one, list_two)
        self.assertEqual(expected, actual)

    def test_sorted_merge_list_of_upper_and_lowercase(self):
        list_two = ['January', 'February']
        list_one = ['march', 'april']
        expected = ['January', 'February', 'march', 'april']
        actual = merge(list_one, list_two)
        self.assertEqual(expected, actual)

    def test_sorted_merge_list_overlapping_letter_J(self):
        list_two = ['Chloe', 'David', 'Jacky']
        list_one = ['Jae', 'Jason', 'Joseph']
        expected = ['Chloe', 'David', 'Jacky', 'Jae', 'Jason', 'Joseph']
        actual = merge(list_one, list_two)
        self.assertEqual(expected, actual)

    def test_sorted_merge_list_of_same_length_elements(self):
        list_two = ['Chl', 'Dav', 'Jac']
        list_one = ['Jae', 'Jas', 'Jos']
        expected = ['Chl', 'Dav', 'Jac', 'Jae', 'Jas', 'Jos']
        actual = merge(list_one, list_two)
        self.assertEqual(expected, actual)

    def test_sorted_merge_long_list_of_names_no_overlapping_letter(self):
        list_two = ['Amy', 'Bob', 'Chloe', 'David', 'Emerald', 'Frances', 'George', 'Hertie']
        list_one = ['Jacky', 'Jae', 'James', 'Janelle', 'Jasmine', 'Jason', 'Jolene', 'Joseph']
        expected = ['Amy', 'Bob', 'Chloe', 'David', 'Emerald', 'Frances', 'George', 'Hertie', 'Jacky', 'Jae', 'James',
                    'Janelle', 'Jasmine', 'Jason', 'Jolene', 'Joseph']
        actual = merge(list_one, list_two)
        self.assertEqual(expected, actual)
