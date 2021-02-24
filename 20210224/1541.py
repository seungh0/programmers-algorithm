import unittest


def solution(param):
    add = param.split('-')
    total = 0
    for i in range(len(add)):
        nums = map(int, add[i].split("+"))
        temp = sum(nums)
        if i == 0:
            total += temp
        else:
            total -= temp
    return total


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("55-50+40-60+40")
        self.assertEqual(result, -135)

    def test_something1(self):
        result = solution("55-50+40")
        self.assertEqual(result, -35)


if __name__ == '__main__':
    unittest.main()
