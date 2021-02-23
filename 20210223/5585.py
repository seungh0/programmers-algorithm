import unittest


def solution(money):
    coins = [500, 100, 50, 10, 5, 1]
    changes = 1000 - money
    cnt = 0
    for i in coins:
        tmp = changes // i
        if tmp > 0:
            changes -= tmp * i
            cnt += tmp
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(380)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
