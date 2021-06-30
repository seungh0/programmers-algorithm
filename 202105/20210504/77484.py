import unittest

prizes = [6, 6, 5, 4, 3, 2, 1]


def solution(lottos, win_nums):
    cnt = 0
    dontcare = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
    return [prizes[cnt + dontcare], prizes[cnt]]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
        self.assertEqual(result, [3, 5])

    def test_something1(self):
        result = solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
        self.assertEqual(result, [1, 6])


if __name__ == '__main__':
    unittest.main()
