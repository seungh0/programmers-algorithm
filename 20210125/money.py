import unittest

d = [10001] * 10000


def solution(total, arr):
    d[0] = 0
    for i in range(len(arr)):
        for j in range(arr[i], total + 1):
            if d[j - arr[i]] != 10001:
                d[j] = min(d[j], d[j - arr[i]] + 1)
    if d[total == 10001]:
        return -1
    return d[total]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(15, [2, 3])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
