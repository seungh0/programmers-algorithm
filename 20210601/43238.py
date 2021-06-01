import unittest


def solution(n, times):
    left, right = 1, max(times) * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        people = 0
        for i in times:
            people += mid // i
            if people >= n:
                right = mid - 1
                answer = mid
                break
        if people < n:
            left = mid + 1
    return answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(6, [7, 10])
        self.assertEqual(result, 28)


if __name__ == '__main__':
    unittest.main()
