import unittest


def solution(arr):
    arr.sort()
    target = 1
    for x in arr:
        if target < x:
            break
        target += x
    return target


class TestCase(unittest.TestCase):
    def test_case_1(self):
        arr = [3, 2, 1, 1, 9]
        result = solution(arr)
        self.assertEqual(result, 8)
