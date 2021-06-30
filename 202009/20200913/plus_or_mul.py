import unittest


def solution(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        if arr[i - 1] <= 1 or arr[i] <= 1:
            result += arr[i]
        else:
            result *= arr[i]
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [0, 2, 9, 8, 4]
        result = solution(arr)
        self.assertEqual(result, 576)

    def test_something2(self):
        arr = [5, 6, 7]
        result = solution(arr)
        self.assertEqual(result, 210)

    def test_something3(self):
        arr = [1, 1, 1]
        result = solution(arr)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
