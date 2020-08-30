import unittest


def solution(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    solution(arr, start, right - 1)
    solution(arr, right + 1, end)
    return arr


class QuickSortTest(unittest.TestCase):
    def test_case_1(self):
        arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
        result = solution(arr, 0, len(arr) - 1)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
