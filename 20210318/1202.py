import unittest
import heapq
import sys

input = sys.stdin.readline


def solution(n, m):
    bags = []
    for i in m:
        heapq.heappush(bags, i)
    jewelries = []
    for i in n:
        heapq.heappush(jewelries, i)

    result = 0
    temp = []
    while bags:
        bag = heapq.heappop(bags)

        while jewelries and bag >= jewelries[0][0]:
            heapq.heappush(temp, -(heapq.heappop(jewelries)[1]))  # 어짜피 남은 것은 들어가있고 쓸 수 있음

        if temp:
            result += -(heapq.heappop(temp))
    return result


# n, m = map(int, input().split())
# bags = []
# jews = []
# for i in range(n):
#     jews.append(list(map(int, input().split())))
# for i in range(m):
#     bags.append(int(input()))
# print(solution(jews, bags))


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
