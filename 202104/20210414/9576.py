import unittest
import sys

input = sys.stdin.readline


def solution(n, m, request):
    request.sort(key=lambda x: x[1])
    books = [False for _ in range(n + 1)]
    books[0] = True

    result = 0
    while request:
        start, end = request.pop()
        for i in range(start, end + 1):
            if not books[i]:
                result += 1
                books[i] = True
                break
    return result


# n = int(input())
# for i in range(n):
#     books = []
#     n, m = map(int, input().split())
#     for j in range(m):
#         books.append(list(map(int, input().split())))
#     print(solution(n, m, books))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(2, 3, [
            [1, 2], [1, 2], [1, 2]
        ])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
