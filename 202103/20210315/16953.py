import unittest


def solution(fr, to):
    cnt = 1
    while fr != to:
        if fr > to:
            cnt = -1
            break
        elif to % 10 == 1:
            to = to // 10
            cnt += 1
        elif to % 2 == 0:
            to /= 2
            cnt += 1
        else:
            cnt = -1
            break
    return cnt


# fr, to = map(int, input().split(" "))
# print(solution(fr, to))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(2, 162)
        self.assertEqual(result, 5)

    def test_something1(self):
        result = solution(4, 42)
        self.assertEqual(result, -1)

    def test_something2(self):
        result = solution(100, 40021)
        self.assertEqual(result, 5)

    def test_something3(self):
        result = solution(2, 1)
        self.assertEqual(result, -1)

    def test_something4(self):
        result = solution(1, 3)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
