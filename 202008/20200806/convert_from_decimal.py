import unittest


def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number // base
    return result


class TestCase(unittest.TestCase):
    def test_base_2(self):
        number, base = 9, 2
        self.assertEqual(convert_to_decimal(number, base), 1001)

    def test_base_8(self):
        number, base = 73, 8
        self.assertEqual(convert_to_decimal(number, base), 111)


if __name__ == "__main__":
    unittest.main()
