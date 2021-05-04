import unittest


def init(rows, columns):
    arr = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = cnt
            cnt += 1
    return arr


def rotate(arr, sx, sy, ex, ey):
    sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1
    x = ex - sx  # 3
    y = ey - sy  # 2
    min_value = arr[sx][sy]
    init_value = arr[sx][sy]

    for i in range(sx, sx + x, 1):
        next = arr[i + 1][sy]
        arr[i][sy] = next
        min_value = min(min_value, next)

    for i in range(sy, sy + y, 1):
        next = arr[ex][i + 1]
        arr[ex][i] = next
        min_value = min(min_value, next)

    for i in range(ex, ex - x, -1):
        next = arr[i - 1][ey]
        arr[i][ey] = next
        min_value = min(min_value, next)

    for i in range(ey, ey - y, -1):
        next = arr[sx][i - 1]
        arr[sx][i] = next
        min_value = min(min_value, next)
    arr[sx][sy + 1] = init_value
    return arr, min_value


def solution(rows, columns, queries):
    arr = init(rows, columns)
    result = []
    for query in queries:
        sx, sy, ex, ey = query
        arr, min_value = rotate(arr, sx, sy, ex, ey)
        result.append(min_value)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
        self.assertEqual(result, [8, 10, 25])

    def test_something1(self):
        result = solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])
        self.assertEqual(result, [1, 1, 5, 3])

    def test_something2(self):
        result = solution(100, 97, [[1, 1, 100, 97]])
        self.assertEqual(result, [1])
        if __name__ == '__main__':
            unittest.main()
