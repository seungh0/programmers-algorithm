import unittest


def solution(height, width):
    if height == 1:
        return 1
    if height == 2:
        return min(4, (width + 1) // 2)
    else:
        if width < 7:
            return min(4, width)
        else:
            return width - 2


# n, m = map(int, input().split(" "))
# print(solution(n, m))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(100, 50)
        self.assertEqual(result, 48)

    def test_something1(self):
        result = solution(1, 1)
        self.assertEqual(result, 1)

    def test_something2(self):
        result = solution(17, 5)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
