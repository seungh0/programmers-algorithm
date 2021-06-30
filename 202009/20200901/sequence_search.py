import unittest


def solution(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1
    return -1


class SequenceSearchTest(unittest.TestCase):
    def test_case_1(self):
        array = ['ABC', 'DEF', 'ERG', 'DFA']
        target = 'ERG'
        result = solution(array, target)
        self.assertEqual(result, 3)
