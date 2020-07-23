# 가장 큰 수 (Level2)
# https://programmers.co.kr/learn/courses/30/lessons/42746

import unittest


class Value:
    def __init__(self, value):
        self.value = str(value)

    def __lt__(self, other):
        return self.compare(other) == -1

    def __gt__(self, other):
        return self.compare(other) == 1

    def __eq__(self, other):
        return self.compare(other) == 0

    def compare(self, other):
        t1 = int(self.value + other.value)
        t2 = int(other.value + self.value)
        return (t1 > t2) - (t1 < t2)


def makeSentence(arr):
    answer = ""
    for i in arr:
        answer += i.value
    return str(int(answer))


def solution(numbers):
    arr = [Value(x) for x in numbers]
    arr.sort(reverse=True)
    return makeSentence(arr)


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        numbers = [6, 10, 2]
        # when
        result = solution(numbers)
        # then
        self.assertEqual(result, "6210")

    def test_case2(self):
        # given
        numbers = [100, 20, 3]
        # when
        result = solution(numbers)
        # then
        self.assertEqual(result, "320100")


if __name__ == '__main__':
    unittest.main()
