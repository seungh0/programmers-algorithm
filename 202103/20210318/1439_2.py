import unittest


def solution(value):
    cnt = 0
    for i in range(1, len(value)):
        if value[i - 1] != value[i]:
            cnt += 1
    return (cnt + 1) // 2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("0001100")
        self.assertEqual(result, 1)

    def test_something1(self):
        result = solution("01")
        self.assertEqual(result, 1)

    def test_something2(self):
        result = solution("010")
        self.assertEqual(result, 1)

    def test_something3(self):
        result = solution("0101")
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
