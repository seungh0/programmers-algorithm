import unittest


def solution(arr):
    min_arr = []
    for i in range(len(arr)):
        min_value = 10000
        for j in range(len(arr[i])):
            if arr[i][j] < min_value:
                min_value = arr[i][j]
        min_arr.append(min_value)
    return max(min_arr)


def solution1(arr):
    result = 0
    for i in arr:
        min_val = min(i)
        result = max(result, min_val)
    return result


class TestCase(unittest.TestCase):
    def test_case_1(self):
        arr = [
            [3, 1, 2],
            [4, 1, 4],
            [2, 2, 2]
        ]
        result = solution(arr)
        self.assertEqual(result, 2)

    def test_case_2(self):
        arr = [
            [7, 3, 1, 8],
            [3, 3, 3, 4]
        ]
        result = solution(arr)
        self.assertEqual(result, 3)

    def test_case_3(self):
        arr = [
            [3, 1, 2],
            [4, 1, 4],
            [2, 2, 2]
        ]
        result = solution1(arr)
        self.assertEqual(result, 2)

    def test_case_4(self):
        arr = [
            [7, 3, 1, 8],
            [3, 3, 3, 4]
        ]
        result = solution1(arr)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
