import unittest


def solution(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


class SelectionSortTest(unittest.TestCase):
    def test_case_1(self):
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        result = solution(array)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
