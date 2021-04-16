import unittest


def solution(param):
    result = ""
    prev = param[0]
    for i in param:
        if i != prev:
            result += prev
            prev = i
    result += prev
    return min(result.count('0'), result.count('1'))


# val = input()
# print(solution(val))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("0001100")
        self.assertEqual(result, 1)

    def test_something1(self):
        result = solution("00110011")
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
