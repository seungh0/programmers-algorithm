import unittest


def solution(array):
    count = [0] * (max(array) + 1)
    for i in array:
        count[i] += 1

    result = []
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)
            
    return result


class CountSortTest(unittest.TestCase):
    def test_case_1(self):
        array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
        result = solution(array)

        self.assertEqual(result, [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9])


if __name__ == "__main__":
    unittest.main()
