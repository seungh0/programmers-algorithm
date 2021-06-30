import unittest


def is_prime_number(n):
    if n < 3:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


class TestCase(unittest.TestCase):
    def test_prime_number_case_1(self):
        n = 17
        self.assertTrue(is_prime_number(n))

    def test_prime_number_case_2(self):
        n = 3
        self.assertTrue(is_prime_number(n))

    def test_prime_number_case_3(self):
        n = 2
        self.assertTrue(is_prime_number(n))

    def test_prime_number_case_4(self):
        n = 4
        self.assertFalse(is_prime_number(n))


if __name__ == "__main__":
    unittest.main()
