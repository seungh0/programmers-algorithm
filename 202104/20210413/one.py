import unittest

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']


def solution(param):
    result = ''
    while param > 0:
        n = param % 16
        param -= n * 16
        result += str(num[n])
    return result[::-1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(15)
        self.assertEqual(result, 'F')

    def test_something1(self):
        result = solution(17)
        self.assertEqual(result, '11')


if __name__ == '__main__':
    unittest.main()
