import unittest
import heapq


def solution(param):
    q = []
    for i in param:
        heapq.heappush(q, i)

    result = 0
    while len(q) > 1:
        left = heapq.heappop(q)
        right = heapq.heappop(q)
        total = left + right
        result += total
        heapq.heappush(q, total)
    return result


# n = int(input())
# r = []
# for i in range(n):
#     r.append(int(input()))
# print(solution(r))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([10, 20, 40])
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()
