import unittest


def sol_count(arr, dif):
    cnt = 0
    i = 0
    while i < len(arr):
        if arr[i] == dif:
            while i < len(arr) and arr[i] == dif:
                i += 1
            cnt += 1
        i += 1
    return cnt


def solution(arr):
    result = []
    num = [0, 1]
    for i in num:
        result.append(sol_count(arr, i))
    return min(result)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [0, 0, 0, 1, 1, 0, 0]
        result = solution(arr)
        self.assertEqual(result, 1)

    def test_something2(self):
        arr = [1, 0, 0, 0, 0, 0, 1]
        result = solution(arr)
        self.assertEqual(result, 1)

    def test_something3(self):
        arr = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
        result = solution(arr)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
