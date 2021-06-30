import unittest

base = ['1', '2', '4']


def solution(n):
    if n <= 3:
        return base[n - 1]
    share, rest = divmod(n - 1, 3)
    return solution(share) + base[rest]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(7)
        self.assertEqual(result, '21')

    def test_something2(self):
        result = solution(6)
        self.assertEqual(result, '14')


if __name__ == '__main__':
    unittest.main()
