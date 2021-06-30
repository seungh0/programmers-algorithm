import unittest
import sys

input = sys.stdin.readline


def cnt(length, numbers):
    total = 0
    for i in numbers:
        if i > length:
            total += i - length
    return total


def solution(n, target, numbers):
    start, end = 0, max(numbers)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        value = cnt(mid, numbers)
        if value >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


n, m = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
print(solution(n, m, numbers))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, 7, [20, 15, 10, 17])
        self.assertEqual(result, 15)

    def test_something2(self):
        result = solution(4, 11, [20, 15, 10, 15])
        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()
