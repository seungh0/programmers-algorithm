import unittest

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def solution(value, base):
    answer = ''
    while value > 0:
        answer += a[value % base]
        value = value // base
    return answer[::-1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(17, 16)
        self.assertEqual(result, '11')

    def test_something1(self):
        result = solution(10, 4)
        self.assertEqual(result, '22')


if __name__ == '__main__':
    unittest.main()
