import unittest
from unittest.mock import patch

from src.reduce_sum.answer import numbers, sum_numbers
import src.reduce_sum.answer


class TestReduce(unittest.TestCase):

    @patch('src.reduce_sum.answer.other')
    def test_result_mock_other(self, mock_other):
        r = sum_numbers(numbers)
        self.assertEqual(r, 96)
        mock_other.assert_called()

    @patch('src.reduce_sum.answer.other')
    def test_result_mock_other_and_reduce(self, mock_other):
        with patch.object(src.reduce_sum.answer, 'reduce') as reduce_mock:
            reduce_mock.return_value = 96
            r = sum_numbers(numbers)
            self.assertEqual(r, 96)
            mock_other.assert_called()
            reduce_mock.assert_called()
