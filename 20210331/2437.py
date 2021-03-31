import unittest


def solution(n, array):
    array.sort()
    n = 1
    for i in array:
        if n < i:
            break
        n += i
    return n


n = int(input())
array = list(map(int, input().split()))
print(solution(n, array))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(7, [3, 1, 6, 2, 7, 30, 1])
        self.assertEqual(result, 21)

    def test_something1(self):
        result = solution(4, [1, 1, 1, 5])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
