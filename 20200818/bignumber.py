import unittest


def find_biggest(number):
    max_index = 0
    for i in range(len(number)):
        if number[max_index] < number[i]:
            max_index = i
    return int(number.pop(max_index))


def calculate(M, K, numbers):
    biggest = find_biggest(numbers)
    biggest_2 = find_biggest(numbers)

    s = K * biggest + biggest_2
    return s * (M // (K + 1)) + biggest * (M % (K + 1))


def solution():
    n, m, k = map(int, input().split(" "))
    numbers = list(map(int, input().split(" ")))
    print(calculate(m, k, numbers))


class UnitTest(unittest.TestCase):
    def test_calculate(self):
        M = 8
        K = 3
        numbers = [2, 4, 5, 4, 6]
        self.assertEqual(calculate(M, K, numbers), 46)


if __name__ == "__main__":
    unittest.main()
