import unittest


def calculate_2(m, k, numbers):
    numbers.sort(reverse=True)
    first, second = numbers[0], numbers[1]
    result = 0
    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1
    return result


def calculate(m, k, numbers):
    numbers.sort(reverse=True)
    first, second = numbers[0], numbers[1]
    unit = k * first + second
    return unit * (m // (k + 1)) + first * (m % (k + 1))


def solution():
    n, m, k = map(int, input().split(" "))
    numbers = list(map(int, input().split(" ")))
    print(calculate(m, k, numbers))


class UnitTest(unittest.TestCase):
    def test_calculate(self):
        m, k = 8, 3
        numbers = [2, 4, 5, 4, 6]
        self.assertEqual(calculate(m, k, numbers), 46)

    def test_calculate2(self):
        m, k = 8, 3
        numbers = [2, 4, 5, 4, 6]
        self.assertEqual(calculate_2(m, k, numbers), 46)


if __name__ == "__main__":
    unittest.main()
