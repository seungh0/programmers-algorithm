import unittest


def cut(arr, mid):
    sum = 0
    for i in range(len(arr)):
        if arr[i] - mid > 0:
            sum += arr[i] - mid
    return sum


def binary_search(arr, target):
    start = 0
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2
        total = cut(arr, mid)

        if total == target:
            return mid

        elif total > target:
            start = mid + 1
            
        else:
            end = mid - 1
    return -1


def solution(arr, target):
    arr.sort()
    return binary_search(arr, target)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [19, 15, 10, 17]
        result = solution(arr, 6)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
