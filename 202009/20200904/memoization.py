import unittest


# 2의 99승으로 시간초과.
def not_working_solution(n):
    if n == 1 or n == 2:
        return 1
    return solution(n - 1) + solution(n - 2)


# 캐싱해서 사용해서 시간 개선

d = [0] * 100


def solution(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = solution(n - 1) + solution(n - 2)
    return d[n]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = 99
        result = solution(a)
        self.assertEqual(result, 218922995834555169026)


if __name__ == '__main__':
    unittest.main()
