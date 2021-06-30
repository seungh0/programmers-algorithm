import unittest


def find_index(array):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def solution(array):
    return find_index(array)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([-15, -6, 1, 3, 7])
        self.assertEqual(result, 3)

    def test_something1(self):
        result = solution([-15, -4, 2, 8, 9, 13, 15])
        self.assertEqual(result, 2)

    def test_something2(self):
        result = solution([-15, -4, 3, 8, 9, 13, 15])
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
