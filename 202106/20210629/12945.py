import unittest


def solution(n):
    answer = [0] * (n + 1)
    for i in range(n + 1):
        if i <= 1:
            answer[i] = i
        else:
            answer[i] = answer[i - 1] + answer[i - 2]
    return answer[n] % 1234567


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(3)
        self.assertEqual(result, 2)

    def test_something1(self):
        result = solution(5)
        self.assertEqual(result, 5)

    def test_something2(self):
        result = solution(0)
        self.assertEqual(result, 0)

    def test_something3(self):
        result = solution(2)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
