import unittest


def get_total(param):
    total = 0
    i = 0
    while i < len(param):
        if i + 1 < len(param):
            if param[i] * param[i + 1] > param[i] + param[i + 1]:
                total += param[i] * param[i + 1]
            else:
                total += param[i] + param[i + 1]
            i += 2
        else:
            total += param[i]
            i += 1
    return total


def solution(plus, minus):
    plus.sort(reverse=True)
    minus.sort()
    total = 0
    total += get_total(plus)
    total += get_total(minus)
    return total


n = int(input())
plus = []
minus = []
for i in range(n):
    n = int(input())
    if n >= 1:
        plus.append(n)
    else:
        minus.append(n)
print(solution(plus, minus))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([2, 1, 3], [-1])
        self.assertEqual(result, 6)

    def test_something1(self):
        result = solution([1, 2, 4, 3, 5], [0])
        self.assertEqual(result, 27)

    def test_something3(self):
        result = solution([], [-1, -2, -3])
        self.assertEqual(result, 5)

    def test_something4(self):
        result = solution([], [0, -2])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
