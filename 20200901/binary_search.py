import unittest


def binary_search(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    return mid


def binary_search_2(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = binary_search(arr, 5, 0, len(arr) - 1)
        self.assertEqual(result, 2)

    def test_something_1(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = binary_search(arr, 4, 0, len(arr) - 1)
        self.assertEqual(result, -1)

    def test_something_solution_1(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = binary_search_2(arr, 5, 0, len(arr) - 1)
        self.assertEqual(result, 2)

    def test_something_solution_2(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = binary_search_2(arr, 4, 0, len(arr) - 1)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
