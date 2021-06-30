# 프린터 (Level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42587
import unittest

NOT_FOUND = -1
START_COUNT = 1
EMPTY = -1000000


def solution(priorities, location):
    queue = make_sorted_queue(priorities)
    return findIndex(queue, location)


def make_sorted_queue(priorities):
    index = 0
    queue = []
    for _ in priorities:
        index = findMaxIndex(priorities, index)
        queue.append(index)
        priorities[index] = EMPTY  # to maintain the index, insert EMPTY number
    return queue


def findMaxIndex(arr, start_idx):
    max_value = arr[start_idx]
    index = start_idx
    for _ in arr:
        if max_value < arr[start_idx]:
            max_value = arr[start_idx]
            index = start_idx
        start_idx = increase(start_idx, arr)
    return index


# make 0 when index is out of range
def increase(index, arr):
    index += 1
    if index >= len(arr):
        index = 0
    return index


def findIndex(queue, location):
    for i in range(len(queue)):
        if queue[i] == location:
            return i + START_COUNT
    return NOT_FOUND


class UnitTest(unittest.TestCase):
    def test_findMax_From_Start_Index_case1(self):
        # given
        arr = [1, 1, 1, 1]

        # when
        result = findMaxIndex(arr, 2)

        # then
        self.assertEqual(result, 2)

    def test_findMax_From_Start_Index_case2(self):
        # given
        arr = [2, 1, 3, 1]

        # when
        result = findMaxIndex(arr, 0)

        # then
        self.assertEqual(result, 2)

    def test_findIndex(self):
        arr = [1, 2, 3, 4]
        result = findIndex(arr, 2)
        self.assertEqual(result, 2)

    def test_findIndex_case_not_found(self):
        arr = [1, 2, 3, 4]
        result = findIndex(arr, 5)
        self.assertEqual(result, NOT_FOUND)


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        priorities = [2, 1, 3, 2]
        location = 2

        # when
        result = solution(priorities, location)

        # then
        self.assertEqual(result, 1)

    def test_case2(self):
        # given
        priorities = [1, 1, 9, 1, 1, 1]
        location = 0

        # when
        result = solution(priorities, location)

        # then
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
