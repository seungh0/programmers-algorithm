import unittest


# def solution(temperatures):
#     result = [0 for _ in range(len(temperatures))]
#     for i in range(len(temperatures) - 1):
#         cnt = 1
#         for j in range(i + 1, len(temperatures)):
#             if temperatures[i] < temperatures[j]:
#                 result[i] = cnt
#                 break
#             cnt += 1
#     return result


def solution(temperatures):
    result = [0 for _ in temperatures]
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([73, 74, 75, 71, 69, 72, 76, 73])
        self.assertEqual(result, [1, 1, 4, 2, 1, 1, 0, 0])


if __name__ == '__main__':
    unittest.main()
