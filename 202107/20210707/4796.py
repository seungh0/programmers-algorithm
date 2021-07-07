import unittest


def solution(l, p, days):
    result = 0
    while days > 0:
        if days >= p:
            result += l
            days -= p
        else:
            result += min(l, days)
            days = 0
    return result


cnt = 1
while True:
    l, p, days = map(int, input().split())
    if l == 0 and p == 0 and days == 0:
        break
    print("Case {}: {}".format(cnt, solution(l, p, days)))
    cnt += 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, 8, 20)
        self.assertEqual(result, 14)

    def test_something1(self):
        result = solution(5, 8, 17)
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
