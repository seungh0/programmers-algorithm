import unittest


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def solution(w, h):
    return w * h - w - h + gcd(w, h)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(8, 12)
        self.assertEqual(result, 80)


if __name__ == '__main__':
    unittest.main()
