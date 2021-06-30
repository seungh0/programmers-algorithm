import unittest


def solution(n, rooms):
    rooms.sort(key=lambda x: (x[1], x[0]))

    last = 0
    cnt = 0
    for start, end in rooms:
        if start >= last:
            last = end
            cnt += 1
    return cnt


# n = int(input())
# rooms = []
# for i in range(n):
#     start, end = map(int, input().split())
#     rooms.append((start, end))
# print(solution(n, rooms))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(11, [
            (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)
        ])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
