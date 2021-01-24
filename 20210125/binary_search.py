import unittest


def binary_search_2(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return binary_search_2(array, target, start, mid - 1)
    else:
        return binary_search_2(array, target, mid + 1, end)


def solution2(array, target):
    return binary_search_2(array, target, 0, len(array))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def solution(array, target):
    return binary_search(array, target, 0, len(array))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 7
        result = solution(array, target)
        self.assertEqual(result, 4)

    def test_something1(self):
        array = [1, 3, 5, 8, 9, 11, 13, 15, 17, 19]
        target = 7
        result = solution(array, target)
        self.assertEqual(result, -1)

    def test_something2(self):
        array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 7
        result = solution2(array, target)
        self.assertEqual(result, 4)

    def test_something3(self):
        array = [1, 3, 5, 8, 9, 11, 13, 15, 17, 19]
        target = 7
        result = solution2(array, target)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
