import unittest


def solution(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return solution(left) + [pivot] + solution(right)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        result = solution(array)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
