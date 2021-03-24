import unittest


def solution(nums):
    max_cnt = len(nums) // 2
    n = list(set(nums))
    return min(max_cnt, len(n))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([3, 1, 2, 3])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
