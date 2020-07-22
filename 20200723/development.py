# 기능 개발 (Level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42586
import unittest


def solution(progresses, speeds):
    result = []
    while len(progresses) > 0:
        __plusProgress(progresses, speeds)
        if progresses[0] >= 100:
            result.append(__getAmountOfDone(progresses, speeds))
    return result


def __plusProgress(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i] += speeds[i]


def __getAmountOfDone(progresses, speeds):
    amount = 0
    while len(progresses) > 0:
        if progresses[0] < 100:
            break
        speeds.pop(0)
        progresses.pop(0)
        amount += 1
    return amount


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        progresses = [93, 30, 55]
        speeds = [1, 30, 5]
        # when
        result = solution(progresses, speeds)
        # then
        self.assertEqual(result, [2, 1])

    def test_case2(self):
        # given
        progresses = [40, 93, 30, 55, 60, 65]
        speeds = [60, 1, 30, 5, 10, 7]
        # when
        result = solution(progresses, speeds)
        # then
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
