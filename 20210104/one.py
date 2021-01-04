import unittest


def dfs(index, numbers, total, target):
    cnt = 0
    if index >= len(numbers):
        if total == target:
            return 1
        return 0

    one = total + numbers[index]
    two = total - numbers[index]

    cnt += dfs(index + 1, numbers, one, target)
    cnt += dfs(index + 1, numbers, two, target)

    return cnt


def solution(numbers, target):
    return dfs(0, numbers, 0, target)


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        numbers = [1, 1, 1, 1, 1]
        result = solution(numbers, 3)
        self.assertEqual(result, 5)

    def test_something2(self):
        numbers = [1, 1]
        result = solution(numbers, 0)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
