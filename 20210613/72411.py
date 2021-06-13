import unittest
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order), c)
        counter = Counter(temp)

        max_value = max(list(counter.values()))
        if max_value >= 2:
            for key, value in counter.items():
                if counter[key] == max_value:
                    answer.append("".join(key))
    return sorted(answer)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
        self.assertEqual(result, ["AC", "ACDE", "BCFG", "CDE"])


if __name__ == '__main__':
    unittest.main()
