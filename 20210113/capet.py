import unittest
import math


def find_divisor(yellow):
    factors = []
    for i in range(1, int(math.sqrt(yellow) + 1)):
        if yellow % i == 0:
            factors.append((yellow // i, i))
    return factors


def count_block(factors):
    return 2 * (factors[0] + factors[1]) + 4


def match_block(divisor, target):
    return count_block(divisor) == target


def find_match_block(divisors, brown):
    for divisor in divisors:
        if match_block(divisor, brown):
            return divisor[0] + 2, divisor[1] + 2
    return -1


def solution(brown, yellow):
    divisors = find_divisor(yellow)
    return find_match_block(divisors, brown)


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        brown = 10
        yellow = 2
        result = solution(brown, yellow)
        self.assertEqual(result, (4, 3))

    def test_something2(self):
        brown = 8
        yellow = 1
        result = solution(brown, yellow)
        self.assertEqual(result, (3, 3))

    def test_something3(self):
        brown = 24
        yellow = 24
        result = solution(brown, yellow)
        self.assertEqual(result, (8, 6))


if __name__ == '__main__':
    unittest.main()
