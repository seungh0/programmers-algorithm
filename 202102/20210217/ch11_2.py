import unittest


def solution(param):
    left = int(param[0])
    for i in range(1, len(param)):
        right = int(param[i])
        if left <= 1 or right <= 1:
            left += right
        else:
            left *= right
    return left


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("02984")
        self.assertEqual(result, 576)

    def test_something1(self):
        result = solution("567")
        self.assertEqual(result, 210)


if __name__ == '__main__':
    unittest.main()
