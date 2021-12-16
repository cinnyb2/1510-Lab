from unittest import TestCase
from sparsevector import sparse_add


class TestSparseAdd(TestCase):
    def test_sparse_add_same_single(self):
        vector_one = {1: 1, 'length': 60}
        vector_two = {'length': 60, 1: 1}
        expected = {1: 2, 'length': 60}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_add_different_single(self):
        vector_one = {1: 1, 'length': 86}
        vector_two = {2: 1, 'length': 86}
        expected = {1: 1, 2: 1, 'length': 86}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_add_overlap(self):
        vector_one = {1: 1, 3: 2, 5: 1, 'length': 70}
        vector_two = {3: 2, 4: 2, 5: 2, 'length': 70}
        expected = {1: 1, 3: 4, 4: 2, 5: 3, 'length': 70}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_add_negative_integer(self):
        vector_one = {1: -6, 'length': 36}
        vector_two = {'length': 36, 7: -9}
        expected = {1: -6, 7: -9, 'length': 36}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_add_negative_and_positive_integer(self):
        vector_one = {1: -6, 2: 4, 'length': 300}
        vector_two = {'length': 300, 1: 1, 2: -2}
        expected = {1: -5, 2: 2, 'length': 300}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_add_sum_to_0(self):
        vector_one = {1: -1, 2: 1, 'length': 86}
        vector_two = {1: 1, 2: -1, 'length': 86}
        expected = {'length': 86}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_add_entries_all_zero(self):
        vector_one = {'length': 268}
        vector_two = {'length': 268}
        expected = {'length': 268}
        actual = sparse_add(vector_one, vector_two)
        self.assertEqual(expected, actual)

