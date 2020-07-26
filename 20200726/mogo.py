# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840
import unittest


def nextIndex(index, end):
    index += 1
    if index == end:
        index = 0
    return index


def solution(answer):
    max_value = 0
    result = []

    student = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    for i in range(len(student)):
        person = student[i]
        count = 0
        index = 0
        for j in range(len(answer)):
            if answer[j] == person[index]:
                count += 1
            index = nextIndex(index, len(person))

        if max_value == count:
            result.append(i + 1)
        elif max_value <= count:
            max_value = count
            result = [i + 1]

    return result


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        answer = [1, 2, 3, 4, 5]
        # when
        result = solution(answer)
        # then
        self.assertEqual(result, [1])

    def test_case2(self):
        # given
        answer = [1, 3, 2, 4, 2]
        # when
        result = solution(answer)
        # then
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
