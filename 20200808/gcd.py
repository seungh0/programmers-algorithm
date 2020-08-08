import unittest


def gcd(a, b):
    result = 0
    while b != 0:
        result = b
        a, b = b, a % b
    return result


class TestCase(unittest.TestCase):
    def test_base_2(self):
        self.assertEqual(gcd(12, 8), 4)

    def test_base_8(self):
        self.assertEqual(gcd(15, 10), 5)


if __name__ == "__main__":
    unittest.main()
