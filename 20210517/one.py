import unittest
import heapq


def solution(param):
    q = []
    for i in range(len(param)):
        for j in range(len(param[i])):
            heapq.heappush(q, param[i][j])
    result = []
    while q:
        result.append(heapq.heappop(q))
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([[1, 4, 5], [1, 3, 4], [2, 6]])
        self.assertEqual(result, [1, 1, 2, 3, 4, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
