import unittest

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def solution(maps, p, r):
    max_kill = 0

    def dfs(x, y, cnt, is_visited):
        answer = 0
        if is_visited[x][y]:
            return 0
        if x < 0 or y < 0 or x >= len(maps) or y >= len(maps[0]):
            return 0
        if cnt == (r // 2):
            return maps[x][y] // 2
            # 반만 더해서 반환해야 한다
        if cnt > ((r - 2) // 2):
            return 0
        if maps[x][y] <= p:
            answer += 1
        is_visited[x][y] = True
        for dx, dy in move:
            mx, my = x + dx, y + dy
            answer += dfs(mx, my, cnt + 1, is_visited)
        return answer

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            is_visited = [[False] * (len(maps) + 1) for _ in range(len(maps[0]) + 1)]
            max_kill = max(max_kill, dfs(i, j, 0, is_visited))
    return max_kill


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19],
                           [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29], [39, 7, 17, 5, 4, 49, 5],
                           [74, 46, 8, 11, 25, 2, 11]],
                          19, 6)
        self.assertEqual(result, 17)


if __name__ == '__main__':
    unittest.main()
