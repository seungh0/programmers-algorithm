import unittest


def solution(param):
    n = len(param) // 2
    param = list(map(int, param))
    if sum(param[:n]) == sum(param[n:]):
        return "LUCKY"
    return "READY"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('123402')
        self.assertEqual(result, 'LUCKY')

    def test_something1(self):
        result = solution('7755')
        self.assertEqual(result, 'READY')


if __name__ == '__main__':
    unittest.main()
