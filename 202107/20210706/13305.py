import unittest


def solution(n, distances, prices):
    total = 0
    current = 1e9
    for distance, price in zip(distances, prices[:-1]):
        current = min(current, price)
        total += current * distance
    return total


# n = int(input())
# prices = list(map(int, input().split()))
# distances = list(map(int, input().split()))
# print(solution(n, prices, distances))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, [2, 3, 1], [5, 2, 4, 1])
        self.assertEqual(result, 18)

    def test_something1(self):
        result = solution(4, [3, 3, 4], [1, 1, 1, 1])
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
