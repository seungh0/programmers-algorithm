import unittest


def solution(arr):
    count = [0] * (max(arr) + 1)

    for i in arr:
        count[i] += 1

    result = []
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 12]
        result = solution(array)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12])


if __name__ == '__main__':
    unittest.main()
