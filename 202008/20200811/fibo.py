import unittest


def solution_1(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def solution(n):
    if n < 2:
        return n
    return solution(n - 2) + solution(n - 1)


def solution_generate():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


# 1 1 2 3 5
class TestCase(unittest.TestCase):
    def test_fibo_case_1(self):
        # given
        n = 5
        # when
        result = solution(n)
        # then
        self.assertEqual(result, 5)

    def test_fibo_case_2(self):
        # given
        n = 5
        # when
        result = solution_1(n)
        # then

        self.assertEqual(result, 5)

    def test_fibo_case_3(self):
        # given
        n = 10
        result = 0
        # when
        fg = solution_generate()
        for _ in range(n):
            result = next(fg)
        # then
        self.assertEqual(result, 55)


if __name__ == "__main__":
    unittest.main()
