import unittest
import sys

input = sys.stdin.readline


def solution(n, c, array):
    array.sort()
    start = array[1] - array[0]
    end = array[-1] - array[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        value = array[0]
        count = 0
        for i in range(1, n):
            if array[i] >= value + mid:
                count += 1

        if count >= c:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
print(solution(n, m, array))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, 3, [1, 2, 8, 4, 9])
        self.assertEqual(result, 3)


# 1 2 4 8 9


if __name__ == '__main__':
    unittest.main()
