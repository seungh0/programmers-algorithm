import unittest


def solution(param):
    param = sorted(list(set(param)))
    return ''.join(param)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("bcabc")
        self.assertEqual(result, "abc")

    def test_something1(self):
        result = solution("cbacdcbc")
        self.assertEqual(result, "acdb")


if __name__ == '__main__':
    unittest.main()
