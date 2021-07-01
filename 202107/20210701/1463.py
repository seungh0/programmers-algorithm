import unittest


def solution(n):
    array = [1e9] * (n + 1)
    array[1] = 0
    for i in range(1, n + 1):
        if i * 3 <= n:
            array[i * 3] = min(array[i * 3], array[i] + 1)
        if i * 2 <= n:
            array[i * 2] = min(array[i * 2], array[i] + 1)
        if i + 1 <= n:
            array[i + 1] = min(array[i + 1], array[i] + 1)
    return array[n]


# n = int(input())
# print(solution(n))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(2)
        self.assertEqual(result, 1)

    def test_something1(self):
        result = solution(10)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
