import unittest


def solution(param):
    param.sort()
    result = []
    for i in range(len(param) - 2):
        for j in range(i + 1, len(param) - 1):
            for z in range(j + 1, len(param)):
                if param[i] + param[j] + param[z] == 0:
                    result.append((param[i], param[j], param[z]))
    return [[x, y, z] for x, y, z in list(set(result))]


def solution1(param):
    param.sort()
    result = []
    for i in range(len(param) - 2):
        if i > 0 and param[i] == param[i - 1]:
            continue
        left, right = i + 1, len(param) - 1
        while left < right:
            sum = param[i] + param[left] + param[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([param[i], param[left], param[right]])
                while left < right and param[left] == param[left + 1]:
                    left += 1
                while left < right and param[right - 1] == param[right]:
                    right -= 1
                left += 1
                right -= 1
    return sorted(result, key=lambda x: (x[0], x[1], x[2]), reverse=True)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([-1, 0, 1, 2, -1, -4])
        self.assertEqual(result, [
            [-1, 0, 1],
            [-1, -1, 2]
        ])

    def test_something1(self):
        result = solution1([-1, 0, 1, 2, -1, -4])
        self.assertEqual(result, [
            [-1, 0, 1],
            [-1, -1, 2]
        ])


if __name__ == '__main__':
    unittest.main()
