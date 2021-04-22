import unittest


def solution(prices):
    result = [0 for _ in prices]
    for i in range(len(prices) - 1):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                cnt += 1
                break
            cnt += 1
        result[i] = cnt
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 2, 3, 2, 3])
        self.assertEqual(result, [4, 3, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
