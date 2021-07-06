import unittest

num = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def calculate(values):
    total = 0
    for i, value in enumerate(values):
        total += value * num[i]
    return total


def solution(n, words):
    dict = {}

    for word in words:
        length = len(word) - 1
        for i, w in enumerate(word):
            if w in dict:
                dict[w] += pow(10, length - i)
            else:
                dict[w] = pow(10, length - i)

    values = sorted(list(dict.values()), reverse=True)
    return calculate(values)


# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(input())
# print(solution(n, nums))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(2, ["AAA", "AAA"])
        self.assertEqual(result, 1998)

    def test_something1(self):
        result = solution(2, ["GCF", "ACDEB"])
        self.assertEqual(result, 99437)


if __name__ == '__main__':
    unittest.main()
