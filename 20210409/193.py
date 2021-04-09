import unittest


def solution1(nums):
    result = []
    p = 1
    for i in nums:
        result.append(p)
        p *= i
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= p
        p *= nums[i]
    return result


def solution(nums):
    result = []
    for i in nums:
        value = 1
        for j in nums:
            if i != j:
                value *= j
        result.append(value)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 2, 3, 4])
        self.assertEqual(result, [24, 12, 8, 6])

    def test_something1(self):
        result = solution1([1, 2, 3, 4])
        self.assertEqual(result, [24, 12, 8, 6])


if __name__ == '__main__':
    unittest.main()
