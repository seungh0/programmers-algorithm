import unittest


def solution(n, params):
    answer = [1e9] * (max(params) + 1)
    answer[1] = 1  # (1)
    answer[2] = 2  # (1 + 1), (2)
    answer[3] = 4  # (1 + 2), (1 + 1 + 1), (2 + 1), (3)

    for i in range(4, max(params) + 1):
        answer[i] = answer[i - 3] + answer[i - 2] + answer[i - 1]

    result = []
    for i in params:
        result.append(answer[i])
    return result


# n = int(input())
# params = []
# for _ in range(n):
#     params.append(int(input()))
# [print(i) for i in solution(n, params)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(3, [4, 7, 10])
        self.assertEqual(result, [7, 44, 274])


if __name__ == '__main__':
    unittest.main()
