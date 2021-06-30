import unittest


def solution(n, m):
    cnt = 0
    while n > 1:
        if n % m == 0:
            n /= m
        else:
            n -= 1
        cnt += 1
    return cnt


class TestCase(unittest.TestCase):
    def test_case_1(self):
        result = solution(25, 5)
        self.assertEqual(result, 2)

    def test_case_2(self):
        result = solution(25, 3)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
