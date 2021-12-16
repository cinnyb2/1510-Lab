from unittest import TestCase
from sparsevector import sparse_dot_product


class TestDotProduct(TestCase):
    def test_sparse_dot_product_multiply_same_index_single_positive_integer(self):
        vector_one = {1: 1, 'length': 60}
        vector_two = {'length': 60, 1: 1}
        expected = 1
        actual = sparse_dot_product(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_multiply_different_index_single_positive_integer(self):
        vector_one = {1: 1, 'length': 86}
        vector_two = {2: 1, 'length': 86}
        expected = 0
        actual = sparse_dot_product(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_multiply_overlap_positive_integer(self):
        vector_one = {1: 1, 3: 2, 5: 1, 'length': 70}
        vector_two = {3: 2, 4: 2, 5: 2, 'length': 70}
        expected = 6
        actual = sparse_dot_product(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_multiply_overlap_negative_integer(self):
        vector_one = {1: -1, 3: -2, 5: -1, 'length': 70}
        vector_two = {3: -2, 4: -2, 5: -2, 'length': 70}
        expected = 6
        actual = sparse_dot_product(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_multiply_negative_integer_at_different_index(self):
        vector_one = {1: -6, 'length': 36}
        vector_two = {'length': 36, 7: -9}
        expected = 0
        actual = sparse_dot_product(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_multiply_negative_integer_at_same_index(self):
        vector_one = {6: -2, 7: -6, 'length': 36}
        vector_two = {'length': 36, 6: -1, 7: -9}
        expected = 56
        actual = sparse_dot_product(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_multiply_negative_and_positive_integer(self):
        vector_one = {1: -6, 2: 4, 'length': 300}
        vector_two = {'length': 300, 1: 1, 2: -2}
        expected = -14
        actual = sparse_dot_product(vector_one, vector_two)
        self.assertEqual(expected, actual)

    def test_sparse_dot_product_vector_entries_all_zero(self):
        vector_one = {'length': 268}
        vector_two = {'length': 268}
        expected = 0
        actual = sparse_dot_product(vector_one, vector_two)
        self.assertEqual(expected, actual)
