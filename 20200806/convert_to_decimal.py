import unittest


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


if __name__ == "__main__":
    unittest.main()
