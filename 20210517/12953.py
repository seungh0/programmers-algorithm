import unittest


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solution(arr):
    arr.sort()
    temp = 1
    for i in range(len(arr)):
        temp = (temp * arr[i]) / (gcd(temp, arr[i]))
    return temp


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([2, 6, 8, 14])
        self.assertEqual(result, 168)


if __name__ == '__main__':
    unittest.main()
