import unittest
from bisect import bisect_left, bisect_right


def solution2(target, array):
    right = bisect_right(array, target)
    left = bisect_left(array, target)
    return right - left


def find_first(target, array, start, end):
    if start > end:
        return None

    while start <= end:
        mid = (start + end) // 2
        if (array[mid] == target) and (mid == 0 or array[mid - 1] < array[mid]):
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1


def find_last(target, array, start, end):
    if start > end:
        return None

    while start <= end:
        mid = (start + end) // 2
        if (array[mid] == target) and (mid == len(array) - 1 or array[mid] < array[mid + 1]):
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


def solution(target, array):
    array.sort()
    first = find_first(target, array, 0, len(array) - 1)
    end = find_last(target, array, 0, len(array) - 1)
    return end - first + 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(2, [1, 1, 2, 2, 2, 2, 3])
        self.assertEqual(result, 4)

    def test_something1(self):
        result = solution2(2, [1, 1, 2, 2, 2, 2, 3])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
