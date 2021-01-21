import unittest


def solution(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        result = solution(array)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
