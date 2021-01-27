import unittest
import heapq


# heapq는 다익스트라 최단 경로 알고리즘을 포함해서 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.
# 리스트
# 삽입 시간 -> O(1)
# 삭제 시간 -> O(N)

# 힙
# 삽입 시간 -> O(log N)
# 삭제 시간 -> O(long N)

# 최대 힙 구현 방법 (내림차순)
def solution_reverse(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


# default: 최소 힙 구현 방법 (오름차순)
def solution(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


class MyTestCase(unittest.TestCase):
    def test_heap(self):
        result = solution([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_heap_reverse(self):
        result = solution_reverse([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
        self.assertEqual(result, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
