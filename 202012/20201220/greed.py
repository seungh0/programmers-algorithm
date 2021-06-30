import unittest


def solution(n):
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
        cnt = n // coin
        n -= cnt * coin
        count += cnt
    return count


class TestCase(unittest.TestCase):
    def test_case_1(self):
        n = 1260
        result = solution(n)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
