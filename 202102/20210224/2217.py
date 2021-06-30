import unittest


def solution(param):
    param.sort(reverse=True)
    value = 0
    for i in range(len(param)):
        a = param[i] * (i + 1)
        if a > value:
            value = a
    return value


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([10, 15])
        self.assertEqual(result, 20)

    def test_something2(self):
        result = solution([10, 15, 30, 40])
        self.assertEqual(result, 60)


if __name__ == '__main__':
    unittest.main()
