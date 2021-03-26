import unittest
import sys

input = sys.stdin.readline


class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def findCount(self, target):
        return self.findRight(target) - self.findLeft(target) + 1

    def findLeft(self, target):
        left = 0
        right = len(self.numbers) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if self.numbers[mid] >= target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

    def findRight(self, target):
        left = 0
        right = len(self.numbers) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if self.numbers[mid] <= target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result


def solution(n, numbers, m, target):
    numbers = Numbers(sorted(numbers))
    result = []
    for i in target:
        result.append(numbers.findCount(i))
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
