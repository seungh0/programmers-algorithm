import unittest

d = [0] * 100


def solution(width):
    d[1] = 1
    d[2] = 3
    for i in range(3, width + 1):
        d[i] = d[i - 2] * 2 + d[i - 1]
    return d[width]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(3)
        self.assertEqual(result, 5)

    def test_something(self):
        result = solution(4)
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
