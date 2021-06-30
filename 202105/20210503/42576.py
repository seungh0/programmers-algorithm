import unittest
import collections


def solution(participant, completion):
    dict = collections.defaultdict(int)
    for par in completion:
        dict[par] += 1
    for par in participant:
        if dict[par] == 0:
            return par
        dict[par] -= 1
    return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
        self.assertEqual(result, "leo")


if __name__ == '__main__':
    unittest.main()
