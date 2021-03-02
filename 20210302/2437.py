import unittest


def solution(param):
    param.sort()
    n = 1
    for i in param:
        if n < i:
            break
        n += i
    return n


# n = int(input())
# r = list(map(int, input().split()))
# print(solution(r))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([3, 1, 6, 2, 7, 30, 1])
        self.assertEqual(result, 21)

    def test_something2(self):
        result = solution([2, 3])
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
