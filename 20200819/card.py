import unittest


def find_min(arr):
    value = arr[0]
    for i in arr:
        if value > i:
            value = i
    return value


def find_max(arr):
    value = arr[0]
    for i in arr:
        if value < i:
            value = i
    return value


def solution(arr):
    min_arr = []
    for i in range(len(arr)):
        min_arr.append(find_min(arr[i]))
    return find_max(min_arr)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [
            [3, 1, 2],
            [4, 1, 4],
            [2, 2, 2]
        ]
        result = solution(arr)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
