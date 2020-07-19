# 완주하지 못한 선수 (Level 1)
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
import unittest


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


class TestFirst(unittest.TestCase):
    def test_case1(self):
        # given
        participant = ["leo", "kiki", "eden"]
        completion = ["eden", "kiki"]
        # when
        result = solution(participant, completion)
        # then
        self.assertEqual(result, "leo")

    def test_case2(self):
        # given
        participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
        completion = ["josipa", "filipa", "marina", "nikola"]
        # when
        result = solution(participant, completion)
        # then
        self.assertEqual(result, "vinko")

    def test_case3(self):
        # given
        participant = ["mislav", "stanko", "mislav", "ana"]
        completion = ["stanko", "ana", "mislav"]
        # when
        result = solution(participant, completion)
        # then
        self.assertEqual(result, "mislav")


if __name__ == '__main__':
    unittest.main()
