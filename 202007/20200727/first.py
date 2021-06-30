# H-Index (Level2)
# https://programmers.co.kr/learn/courses/30/lessons/42747
import unittest


def solution(citations):
    h = max(citations)
    for h in range(h, -1, -1):
        if (count_bigger(citations, h) >= h) & (count_under(citations, h) <= h):
            return h
    return -1


def count_bigger(arr, comp):
    ctn = 0
    for i in arr:
        if i >= comp:
            ctn += 1
    return ctn


def count_under(arr, comp):
    return len(arr) - count_bigger(arr, comp)


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        citations = [3, 0, 6, 1, 5]  # 0 1 4 5 6
        # when
        result = solution(citations)
        # then
        self.assertEqual(result, 3)

    def test_case2(self):
        # given
        citations = [5, 5, 5, 5]
        # when
        result = solution(citations)
        # then
        self.assertEqual(result, 4)

    def test_case3(self):
        # given
        citations = [0, 1, 1, 1, 1, 3, 3, 4]
        # when
        result = solution(citations)
        # then
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
