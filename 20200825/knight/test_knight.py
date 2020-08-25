import unittest
from .main import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('a1')
        self.assertEqual(result, 2)

    def test_something_2(self):
        result = solution('h8')
        self.assertEqual(result, 2)

    def test_something_3(self):
        result = solution('d4')
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
