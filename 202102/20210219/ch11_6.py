# https://programmers.co.kr/learn/courses/30/lessons/42891#

import unittest
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    total = 0
    previous = 0
    length = len(food_times)

    while total + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        total += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - total) % length][1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        food_times = [3, 1, 2]
        k = 5
        result = solution(food_times, k)
        self.assertEqual(result, 1)

    def test_something1(self):
        food_times = [4, 2, 3, 6, 7, 1, 5, 8]
        k = 16
        result = solution(food_times, k)
        self.assertEqual(result, 3)

    def test_something2(self):
        food_times = [3, 1, 1, 1, 2, 4, 3]
        k = 12
        result = solution(food_times, k)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
