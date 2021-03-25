import unittest
import sys

input = sys.stdin.readline


def get_count(mid, numbers):
    total = 0
    for i in numbers:
        total += i // mid
    return total


def solution(n, cnt, numbers):
    start, end = 1, max(numbers)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        answer = get_count(mid, numbers)
        if answer >= cnt:
            result = mid
            start = mid + 1
        if answer < cnt:
            end = mid - 1
    return result


# n, m = map(int, input().split())
# numbers = []
# for i in range(n):
#     numbers.append(int(input()))
# print(solution(n, m, numbers))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, 11, [802, 754, 457, 539])
        self.assertEqual(result, 200)


if __name__ == '__main__':
    unittest.main()
