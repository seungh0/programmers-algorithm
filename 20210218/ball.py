import unittest


def solution(param):
    cnt = 0
    for i in range(len(param)):
        for j in range(i + 1, len(param)):
            if param[i] != param[j]:
                cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 3, 2, 3, 2])
        self.assertEqual(result, 8)

    def test_something1(self):
        result = solution([1, 5, 4, 3, 2, 4, 5, 2])
        self.assertEqual(result, 25)


if __name__ == '__main__':
    unittest.main()
