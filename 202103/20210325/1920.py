import unittest


def is_exists(target, numbers):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == numbers[mid]:
            return 1
        if target > numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0


def solution(n, numbers, m, targets):
    numbers.sort()
    result = []
    for target in targets:
        result.append(is_exists(target, numbers))
    return result


n = int(input())

numbers = list(map(int, input().split(" ")))
m = int(input())
targets = list(map(int, input().split(" ")))

result = solution(n, numbers, m, targets)

for i in result:
    print(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, [4, 1, 5, 2, 3], 5, [1, 3, 7, 9, 5])
        self.assertEqual(result, [1, 1, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
