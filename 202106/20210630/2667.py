import unittest

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def solution(n, array):
    is_visited = [[False] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        cnt = 0
        if i < 0 or j < 0 or i >= n or j >= n:
            return cnt
        if is_visited[i][j] or array[i][j] == 0:
            return cnt
        is_visited[i][j] = True

        for mx, my in move:
            dx, dy = i + mx, j + my
            cnt += dfs(dx, dy)
        return cnt + 1

    answer = []
    for i in range(n):
        for j in range(n):
            if not is_visited[i][j] and array[i][j] == 1:
                answer.append(dfs(i, j))
    return len(answer), sorted(answer)


# n = int(input())
# array = []
# for _ in range(n):
#     array.append(list(map(int, list(input()))))
# cnt, result = solution(n, array)
# print(cnt)
# for i in result:
#     print(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(7, [
            [0, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0]
        ])
        self.assertEqual(result, (3, [7, 8, 9]))


if __name__ == '__main__':
    unittest.main()
