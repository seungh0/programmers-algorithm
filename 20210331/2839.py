import unittest


def solution(param):
    cnt = 0
    while param >= 0:
        if param % 5 == 0:
            cnt += param / 5
            return int(cnt)
        param -= 3
        cnt += 1
    return -1


n = int(input())
print(solution(n))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(18)
        self.assertEqual(result, 4)

    def test_something4(self):
        result = solution(10)
        self.assertEqual(result, 2)

    def test_something1(self):
        result = solution(12)
        self.assertEqual(result, 4)

    def test_something2(self):
        result = solution(4)
        self.assertEqual(result, -1)

    def test_something5(self):
        result = solution(11)
        self.assertEqual(result, 3)

    def test_something6(self):
        result = solution(9)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
