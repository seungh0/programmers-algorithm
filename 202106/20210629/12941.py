import unittest


def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 4, 2], [5, 4, 4])  # 5 + 16 + 8 = 29
        self.assertEqual(result, 29)

    def test_something1(self):
        result = solution([1, 2], [3, 4])
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
