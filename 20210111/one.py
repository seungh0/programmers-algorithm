import unittest


def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def solution(arr, find_arr):
    arr.sort()
    result = []
    for i in find_arr:
        if binary_search(arr, i) == -1:
            result.append(False)
        else:
            result.append(True)
    return result


class MyTestCase(unittest.TestCase):

    def test_something(self):
        arr = [8, 3, 7, 9, 2]
        find_arr = [5, 7, 9]
        result = solution(arr, find_arr)
        self.assertEqual(result, [False, True, True])


if __name__ == '__main__':
    unittest.main()
