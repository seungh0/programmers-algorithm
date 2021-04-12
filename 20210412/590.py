import unittest


def solution1(param):
    result = 0
    for i in range(len(param) - 1):
        if param[i] < param[i + 1]:
            result += param[i + 1] - param[i]
    return result


def solution(param):
    result = 0
    min_val = param[0]
    for i in range(len(param) - 1):
        if param[i] > param[i + 1]:
            result += param[i] - min_val
            min_val = param[i + 1]
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 7)

    def test_something1(self):
        result = solution([7, 1, 8, 4, 7, 5])
        self.assertEqual(result, 10)

    def test_something5(self):
        result = solution([1, 5, 9, 4, 7, 5])
        self.assertEqual(result, 11)

    def test_something2(self):
        result = solution1([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 7)

    def test_something3(self):
        result = solution1([7, 1, 8, 4, 7, 5])
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
