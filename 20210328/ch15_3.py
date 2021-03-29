import unittest


def getCount(array, distance):
    cnt = 0
    value = array[0]
    for i in range(1, len(array)):
        if array[i] >= value + distance:
            value = distance
            cnt += 1
    return cnt


def solution(n, c, array):
    result = 0
    array.sort()

    start = array[1] - array[0]
    end = array[-1] - array[0]

    while start <= end:
        mid = (start + end) // 2
        cnt = getCount(array, mid)
        if cnt >= c:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, 3, [1, 2, 8, 4, 9])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
