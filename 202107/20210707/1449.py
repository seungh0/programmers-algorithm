import unittest
from collections import deque


def solution(n, l, array):
    array.sort()
    queue = deque(array)
    cnt = 0
    while queue:
        cnt += 1
        front = queue.popleft()
        while queue:
            if queue[0] - front + 1 <= l:
                queue.popleft()
            else:
                break
    return cnt


n, m = map(int, input().split())
array = list(map(int, input().split()))
print(solution(n, m, array))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, 2, [1, 2, 100, 101])
        self.assertEqual(result, 2)

    def test_something1(self):
        result = solution(4, 101, [1, 2, 100, 101])
        self.assertEqual(result, 1)

    def test_something2(self):
        result = solution(4, 1, [1, 2, 100, 101])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
