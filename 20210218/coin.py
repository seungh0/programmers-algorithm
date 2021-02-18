import unittest


def solution(param):
    param.sort()
    target = 1
    for i in param:
        if target < i:
            break
        target += i
    return target


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([3, 2, 1, 1, 9])
        self.assertEqual(result, 8)

    def test_something1(self):
        result = solution([3, 2, 1, 9])
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
