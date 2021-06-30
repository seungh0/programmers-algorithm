# https://www.acmicpc.net/problem/2512
import unittest
import sys
input = sys.stdin.readline


def calculate(numbers, mid):
    sum = 0
    for i in numbers:
        sum += min(mid, i)
    return sum


def solution(n, numbers, value):
    left = 0
    right = max(numbers)
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        result = calculate(numbers, mid)
        if result <= value:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


n = int(input())
numbers = list(map(int, input().split()))
value = int(input())
print(solution(n, numbers, value))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, [120, 110, 140, 150], 485)
        self.assertEqual(result, 127)


if __name__ == '__main__':
    unittest.main()
