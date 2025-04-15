import unittest
from main import has_five
class TestHasFive(unittest.TestCase):
    def test_with_five(self):
        self.assertTrue(has_five([1, 2, 5]))

    def test_without_five(self):
        self.assertFalse(has_five([0, 1, 2, 3]))

    def test_empty_list(self):
        self.assertFalse(has_five([]))

if __name__ == '__main__':
    unittest.main()
