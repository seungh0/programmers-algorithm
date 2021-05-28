import unittest
import heapq


def solution(scoville, K):
    q = []
    [heapq.heappush(q, s) for s in scoville]

    cnt = 0
    while q:
        left = heapq.heappop(q)
        if left >= K:
            break
        if not q:
            return -1
        right = heapq.heappop(q) * 2
        cnt += 1
        result = left + right
        heapq.heappush(q, result)
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 2, 3, 9, 10, 12], 7)
        self.assertEqual(result, 2)

    def test_something2(self):
        result = solution([1, 2, 3, 9, 10, 12], 1)
        self.assertEqual(result, 0)

    def test_something3(self):
        result = solution([1], 3)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
