# https://www.acmicpc.net/problem/10816

import unittest
from collections import Counter
import sys

input = sys.stdin.readline


def solution(n, numbers, m, targets):
    s = Counter(numbers)
    result = []
    for target in targets:
        result.append(s[target])
    return result


# n = int(input())
# numbers = list(map(int, input().split()))
# m = int(input())
# targets = list(map(int, input().split()))
# result = solution(n, numbers, m, targets)
# for i in result:
#     print(i, end=" ")


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(10, [6, 3, 2, 10, 10, 10, -10, -10, 7, 3], 8, [10, 9, -5, 2, 3, 4, 5, -10])
        self.assertEqual(result, [3, 0, 0, 1, 2, 0, 0, 2])


if __name__ == '__main__':
    unittest.main()
용