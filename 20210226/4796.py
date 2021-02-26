import unittest


def solution(n, p, v):
    a = v // p
    c = v % p if v % p < n else n
    return a * n + c


# cnt = 1
# while True:
#     n, p, v = map(int, input().split(" "))
#     if n == 0 and p == 0 and v == 0:
#         break
#     print("Case " + str(cnt) + ":", solution(n, p, v))
#     cnt += 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, 8, 20)
        self.assertEqual(result, 14)

    def test_something1(self):
        result = solution(5, 8, 17)
        self.assertEqual(result, 11)

    def test_something2(self):
        result = solution(5, 8, 3)
        self.assertEqual(result, 3)

    def test_something3(self):
        result = solution(2, 8, 3)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
