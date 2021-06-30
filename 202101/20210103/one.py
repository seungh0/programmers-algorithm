import unittest


def is_out_of_range(arr, x, y):
    return x < 0 or x >= len(arr) or y < 0 or y >= len(arr[0])


def dfs(arr, x, y):
    if is_out_of_range(arr, x, y):
        return False

    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(arr, x - 1, y)
        dfs(arr, x + 1, y)
        dfs(arr, x, y - 1)
        dfs(arr, x, y + 1)
        return True
    return False


def solution(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if dfs(arr, i, j):
                cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        result = solution(arr)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
