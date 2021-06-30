import unittest

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def solution(value, base):
    answer = 0
    for i, num in enumerate(value[::-1]):
        answer += a.index(num) * (base ** i)
    return answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('12', 5)
        self.assertEqual(result, 7)

    def test_something1(self):
        result = solution('A', 16)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
