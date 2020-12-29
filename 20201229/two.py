import unittest


def solution(hour):
    cnt = 0
    for i in range(hour + 1):
        for j in range(60):
            for z in range(60):
                if '3' in str(i) + str(j) + str(z):
                    cnt += 1
    return cnt


class TestCase(unittest.TestCase):
    def test_case_1(self):
        result = solution(5)
        self.assertEqual(result, 11475)
