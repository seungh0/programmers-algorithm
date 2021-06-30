import unittest
import heapq


def solution1(cards):
    heap = []
    for i in cards:
        heapq.heappush(heap, i)

    result = 0

    while len(heap) != 1:
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        sum_value = one + two
        result += sum_value
        heapq.heappush(heap, sum_value)
    return result


def solution(cards):
    cards.sort()
    for i in range(1, len(cards)):
        cards[i] = cards[i - 1] + cards[i]
    return sum(cards[1:])


class MyTestCase(unittest.TestCase):
    def test_something3(self):
        result = solution1([10, 20, 40])
        self.assertEqual(result, 100)

    def test_something4(self):
        result = solution1([10, 20, 30, 40])
        self.assertEqual(result, 190)

    def test_something(self):
        result = solution([10, 20, 40])
        self.assertEqual(result, 100)

    def test_something1(self):
        result = solution([10, 20, 30, 40])
        self.assertEqual(result, 190)


if __name__ == '__main__':
    unittest.main()
