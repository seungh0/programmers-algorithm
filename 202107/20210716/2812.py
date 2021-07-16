import unittest
import sys

input = sys.stdin.readline


def solution(n, k, arr):
    stack = []
    for i in range(n):
        while k > 0 and stack and stack[-1] < arr[i]:
            stack.pop()
            k -= 1
        stack.append(arr[i])
    return ''.join(stack[:n - k])


# def solution(n, k, queue):
#     result = []
#     while 0 < k < len(queue):
#         index = queue.index(max(queue[:k + 1]))
#         result.append(queue[index])
#         queue = queue[index + 1:]
#         k -= index
#     result += queue
#     r = ""
#     for i in result:
#         r += str(i)
#     return int(r)


# n, m = map(int, input().split(" "))
# nums = input()
# print(solution(n, m, nums))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, 2, '1924')
        self.assertEqual(result, '94')


if __name__ == '__main__':
    unittest.main()
