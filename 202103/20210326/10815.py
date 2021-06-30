# https://www.acmicpc.net/problem/10815
import unittest
import sys

input = sys.stdin.readline


class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def hasNumber(self, target):
        left = 0
        right = len(self.numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.numbers[mid] == target:
                return True
            elif self.numbers[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


def solution(n, numbers, m, targets):
    numbers = Numbers(sorted(numbers))
    result = []
    for target in targets:
        if numbers.hasNumber(target):
            result.append(1)
        else:
            result.append(0)
    return result


# n = int(input())
# numbers = list(map(int, input().split()))
# m = int(input())
# targets = list(map(int, input().split()))
# result = solution(n, numbers, m, targets)
# for i in result:
#     print(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, [6, 3, 2, 10, -10], 8, [10, 9, -5, 2, 3, 4, 5, -10])
        self.assertEqual(result, [1, 0, 0, 1, 1, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
