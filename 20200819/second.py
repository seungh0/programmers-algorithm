import unittest


def solution(n, k):
    cnt = 0
    while n > 1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(25, 5)
        self.assertEqual(result, 2)

    def test_something2(self):
        result = solution(3, 5)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
