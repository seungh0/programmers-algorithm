import unittest


def solution(arr, find_arr):
    array = [0] * 100000

    for i in arr:
        array[i] += 1

    result = []
    for i in find_arr:
        if array[i] <= 0:
            result.append(False)
        else:
            result.append(True)
    return result


class MyTestCase(unittest.TestCase):

    def test_something(self):
        arr = [8, 3, 7, 9, 2]
        find_arr = [5, 7, 9]
        result = solution(arr, find_arr)
        self.assertEqual(result, [False, True, True])


if __name__ == '__main__':
    unittest.main()
