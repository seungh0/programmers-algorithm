import unittest


def solution(distances, prices):
    result = distances[0] * prices[0]
    min_value = prices[0]
    for i in range(1, len(distances)):
        min_value = min(min_value, prices[i])
        result += min_value * distances[i]
    return result


# n = int(input())
# distances = list(map(int, input().split()))
# prices = list(map(int, input().split()))
# print(solution(distances, prices))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([2, 3, 1], [5, 2, 4, 1])
        self.assertEqual(result, 18)

    def test_something1(self):
        result = solution([3, 3, 4], [1, 1, 1, 1])
        self.assertEqual(result, 10)

    def test_something2(self):
        result = solution([3], [2, 1])
        self.assertEqual(result, 6)

    def test_something3(self):
        result = solution([3], [2, 1])
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
