import unittest


def calculate_length(arr, mid):
    result = 0
    for i in arr:
        if i > mid:
            result += (i - mid)
    return result


def binary_search(arr, total, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    length = calculate_length(arr, mid)
    if length > total:
        return binary_search(arr, total, mid + 1, end)
    elif length < total:
        return binary_search(arr, total, start, mid - 1)
    return mid


def solution(arr, total):
    arr.sort()
    return binary_search(arr, total, 0, max(arr))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        total = 6
        arr = [19, 15, 10, 17]
        result = solution(arr, total)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
