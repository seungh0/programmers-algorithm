import unittest


def solution(value):
    cnt_three = 0

    while True:
        if (value - cnt_three * 3) % 5 == 0:
            return (value - cnt_three * 3) // 5 + cnt_three
        cnt_three += 1
        if cnt_three * 3 == value:
            return cnt_three
        if cnt_three * 3 > value:
            return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(18)
        self.assertEqual(result, 4)

    def test_something1(self):
        result = solution(4)
        self.assertEqual(result, -1)

    def test_something2(self):
        result = solution(6)
        self.assertEqual(result, 2)

    def test_something3(self):
        result = solution(9)
        self.assertEqual(result, 3)

    def test_something4(self):
        result = solution(11)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
