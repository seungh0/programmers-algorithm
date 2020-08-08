import unittest


def convert_to_decimal(number, base):
    convertString = "0123456789ABCDEF"
    if number < base:
        return convertString[number]
    else:
        return convert_to_decimal(number // base, base) + convertString[number % base]


class TestCase(unittest.TestCase):
    def test_base_2(self):
        number, base = 9, 2
        self.assertEqual(convert_to_decimal(number, base), "1001")

    def test_base_8(self):
        number, base = 73, 8
        self.assertEqual(convert_to_decimal(number, base), "111")


if __name__ == "__main__":
    unittest.main()
