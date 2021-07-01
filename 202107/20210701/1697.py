import unittest
from collections import deque


def bfs(start, end, is_visited):
    count = 0
    queue = deque([(start, count)])

    while queue:
        node, count = queue.popleft()
        if is_visited[node]:
            continue
        is_visited[node] = True
        if node == end:
            return count
        count += 1
        if (node * 2) <= 100000:
            queue.append((node * 2, count))
        if (node + 1) <= 100000:
            queue.append((node + 1, count))
        if (node - 1) >= 0:
            queue.append((node - 1, count))
    return count


def solution(start, end):
    is_visited = [False] * 100001
    return bfs(start, end, is_visited)


# n, m = map(int, input().split())
# print(solution(n, m))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, 17)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
