import unittest
import collections


def solution(clothes):
    dict = collections.defaultdict(int)
    for name, type in clothes:
        dict[type] += 1
    cnt = 1
    for i in dict.values():
        cnt *= (i + 1)
    return cnt - 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
