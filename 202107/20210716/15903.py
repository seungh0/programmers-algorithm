import unittest


def solution(n, m, arr):
    for i in range(m):
        arr.sort()
        temp = arr[0] + arr[1]
        arr[0], arr[1] = temp, temp
    return sum(arr)


n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
print(solution(n, m, arr))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(3, 1, [3, 2, 6])
        self.assertEqual(result, 16)


if __name__ == '__main__':
    unittest.main()
