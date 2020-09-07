import unittest


def solution(width):
    d = [0] * 100
    d[0], d[1] = 1, 3
    for i in range(2, width):
        d[i] = d[i - 1] + d[i - 2] * 2
    return d[width - 1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        width = 2
        result = solution(width)
        self.assertEqual(result, 3)

    def test_width_three(self):
        width = 3
        result = solution(width)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
