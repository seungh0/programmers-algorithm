import unittest


def convert_to_decimal_2(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result


def convert_to_decimal(number, base):
    answer = 0
    str_num = str(number)
    for i in reversed(range(len(str_num))):
        answer += int(str_num[i]) * (base ** i)
    return answer


class TestCase(unittest.TestCase):
    def test_base_2(self):
        number, base = 1001, 2
        self.assertEqual(convert_to_decimal(number, base), 9)

    def test_base_8(self):
        number, base = 111, 8
        self.assertEqual(convert_to_decimal(number, base), 73)


class TestCase2(unittest.TestCase):
    def test_base_2(self):
        number, base = 1001, 2
        self.assertEqual(convert_to_decimal_2(number, base), 9)

    def test_base_8(self):
        number, base = 111, 8
        self.assertEqual(convert_to_decimal_2(number, base), 73)


if __name__ == "__main__":
    unittest.main()
