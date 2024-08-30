import unittest
from addition import NegativeNumberError, addition


class StringAdditionTest(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(addition([4, 10, 12]), 26)

    def test_add_negative_number(self):
        with self.assertRaises(NegativeNumberError) as context:
            addition([-1, -2, 3])
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

    def test_add_with_delimiter(self):
        self.assertEqual(addition('\\;n*1,2,3'), 6)

    def test_add_with_negative_number(self):
        with self.assertRaises(NegativeNumberError) as context:
            addition('\\;n*1,-2,3')
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")


if __name__ == '__main__':
    unittest.main()
