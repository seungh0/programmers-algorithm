import unittest


def solution(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return -1


def solution1(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [i, nums[i + 1:].index(complement) + (i + 1)]


def solution2(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_something1(self):
        result = solution1([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_something2(self):
        result = solution2([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])


if __name__ == '__main__':
    unittest.main()
