import unittest


def solution(a, b, count):
    a.sort()
    b.sort(reverse=True)

    for i in range(count):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
    return sum(a)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = [1, 2, 5, 4, 3]
        b = [5, 5, 6, 6, 5]
        result = solution(a, b, 3)
        self.assertEqual(result, 26)


if __name__ == '__main__':
    unittest.main()
