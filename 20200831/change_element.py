import unittest


def solution(cnt, a, b):
    a = sorted(a)
    b = sorted(b, reverse=True)
    for i in range(cnt):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    return sum(a)


class CountSortTest(unittest.TestCase):
    def test_case_1(self):
        cnt = 3
        a = [1, 2, 5, 4, 3]
        b = [5, 5, 6, 6, 5]
        result = solution(cnt, a, b)
        self.assertEqual(result, 26)


if __name__ == "__main__":
    unittest.main()
