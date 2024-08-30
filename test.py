import unittest
# from string_addition import addition

class StringAdditionTest(unittest.TestCase):
    def test_addition(self, st):
        res = addition(st)
        self.assertEqual(st, 4)




if __name__ == '__main__':
    unittest.main()
