import unittest


def solution(hours):
    count = 0
    for h in range(hours + 1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h) + str(m) + str(s):
                    count += 1
    return count


class MyTestCase(unittest.TestCase):
    def test_solution_case_1(self):
        hour = 5
        result = solution(hour)
        self.assertEqual(result, 11475)


if __name__ == '__main__':
    unittest.main()
