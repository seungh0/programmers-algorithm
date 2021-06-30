import unittest


def solution(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        result = solution(array)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
