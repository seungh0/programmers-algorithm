import unittest


def solution(param):
    return sum(param) // len(param)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([5, 1, 7, 9])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
