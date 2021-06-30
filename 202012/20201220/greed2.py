import unittest


def solution(arr, value):
    n, m, k = value
    arr.sort(reverse=True)
    cnt1, cnt2 = m // k, m % k
    return arr[0] * cnt1 * k + arr[1] * cnt2


def solution2(arr, value):
    n, m, k = value
    result = 0
    arr.sort(reverse=True)
    while True:
        for i in range(k):
            if m == 0:
                break
            result += arr[0]
            m -= 1
        if m == 0:
            break
        result += arr[1]
        m -= 1
    return result


class TestCase(unittest.TestCase):
    def test_case_1(self):
        n = [5, 8, 3]
        arr = [2, 4, 5, 4, 6]
        result = solution(arr, n)
        self.assertEqual(result, 46)

    def test_case_2(self):
        n = [5, 8, 3]
        arr = [2, 4, 5, 4, 6]
        result = solution2(arr, n)
        self.assertEqual(result, 46)

    def test_case_3(self):
        n = [5, 3, 3]
        arr = [2, 4, 5, 4, 6]
        result = solution(arr, n)
        self.assertEqual(result, 18)

    def test_case_4(self):
        n = [5, 3, 3]
        arr = [2, 4, 5, 4, 6]
        result = solution2(arr, n)
        self.assertEqual(result, 18)


if __name__ == "__main__":
    unittest.main()
