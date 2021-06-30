import unittest


def solution(arr):
    min_arr = []
    for i in range(len(arr)):
        min_arr.append(min(arr[i]))
    return max(min_arr)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [
            [3, 1, 2],
            [4, 1, 4],
            [2, 2, 2]
        ]
        result = solution(arr)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
