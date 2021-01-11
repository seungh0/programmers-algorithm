import unittest


def solution2(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return solution2(array, target, start, mid - 1)
    else:
        return solution2(array, target, mid + 1, end)


def solution(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = solution(array, 4, 0, len(array))
        self.assertEqual(result, -1)

    def test_something1(self):
        array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = solution(array, 3, 0, len(array) - 1)
        self.assertEqual(result, 2)

    def test_something2(self):
        array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = solution2(array, 4, 0, len(array))
        self.assertEqual(result, -1)

    def test_something13(self):
        array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        result = solution2(array, 3, 0, len(array) - 1)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
