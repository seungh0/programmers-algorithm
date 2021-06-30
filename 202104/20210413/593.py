import unittest
import heapq


def solution(people):
    heap = []
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
    result = []
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
        self.assertEqual(result, [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])


if __name__ == '__main__':
    unittest.main()
