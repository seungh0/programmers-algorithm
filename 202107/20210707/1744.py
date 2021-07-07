import unittest
import sys
from collections import deque

input = sys.stdin.readline


def sumOfArray(pos):
    total = 0
    while pos:
        temp = pos.popleft()
        if pos:
            temp *= pos.popleft()
        total += temp
    return total


def solution(nums):
    positive, negative = [], []
    result = 0
    for num in nums:
        if num <= 0:
            negative.append(num)
        elif num > 1:
            positive.append(num)
        else:
            result += num

    positive.sort(reverse=True)
    negative.sort()

    result += sumOfArray(deque(positive))
    result += sumOfArray(deque(negative))
    return result


n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
print(solution(array))


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        result = solution([0, 1, 2, 4, 3, 5])
        self.assertEqual(result, 27)

    def test_something(self):
        result = solution([-1, 2, 1, 3])
        self.assertEqual(result, 6)

    def test_something2(self):
        result = solution([-3, -2, -1])
        self.assertEqual(result, 5)

    def test_something3(self):
        result = solution([-3, -2, -1, -1])
        self.assertEqual(result, 7)

    def test_something4(self):
        result = solution([-1, -1, -3, -2])
        self.assertEqual(result, 7)

    def test_something5(self):
        result = solution([-3, 0])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
