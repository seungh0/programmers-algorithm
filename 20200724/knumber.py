# K번째 수 (Level 1)
# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

import unittest


def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(sliceAndSortArray(array, i))
    return answer


def sliceAndSortArray(array, command):
    arr = array[command[0] - 1: command[1]]
    custom_sort(arr)  # arr.sort()
    return arr[command[2] - 1]


def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        array = [1, 5, 2, 6, 3, 7, 4]
        commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
        # when
        result = solution(array, commands)
        # then
        self.assertEqual(result, [5, 6, 3])


if __name__ == '__main__':
    unittest.main()
