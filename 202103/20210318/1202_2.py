import unittest
import heapq


def solution(n, m):
    bags = []
    for bag in m:
        heapq.heappush(bags, bag)

    jews = []
    for jew in n:
        heapq.heappush(jews, jew)

    afford = []
    result = 0

    while bags:
        bag = heapq.heappop(bags)

        while jews and jews[0][0] <= bag:
            heapq.heappush(afford, -(heapq.heappop(jews)[1]))

        if afford:
            result += -(heapq.heappop(afford))
        else:
            break
    return result


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        jewelries = [(1, 65), (5, 23), (2, 99)]
        bags = [10, 2]
        result = solution(jewelries, bags)
        self.assertEqual(result, 164)

    def test_something2(self):
        jewelries = [(10, 60), (5, 40), (3, 30)]
        bags = [10]
        result = solution(jewelries, bags)
        self.assertEqual(result, 60)

    def test_something3(self):
        jewelries = [(10, 30), (5, 60), (3, 50)]
        bags = [10, 5]
        result = solution(jewelries, bags)
        self.assertEqual(result, 110)


if __name__ == '__main__':
    unittest.main()
