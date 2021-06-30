# 더 맵게 (Level2)
# https://programmers.co.kr/learn/courses/30/lessons/42626
import unittest
import heapq


def solution(arr, k):
    arr.sort()
    ctn = count(arr, k)
    return ctn


def count(heap, k):
    ctn = 0
    while heap[0] < k:
        if len(heap) <= 1:
            return -1
        ctn += 1
        t1 = heapq.heappop(heap)
        t2 = heapq.heappop(heap)
        heapq.heappush(heap, t1 + t2 * 2)
    return ctn


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        arr = [1, 2, 3, 9, 10, 12]
        # when
        result = solution(arr, 7)
        # then
        self.assertEqual(result, 2)

    def test_case2(self):
        # given
        arr = [1, 2, 3, 9, 10, 12]
        # when
        result = solution(arr, 1000)
        # then
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
