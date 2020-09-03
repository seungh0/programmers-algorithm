import unittest


def solution(item, search):
    arr = [0] * (max(item) + 1)
    for i in item:
        arr[i] += 1

    result = []
    for i in search:
        if arr[i] == 1:
            result.append('yes')
        else:
            result.append('no')

    return result


def binary_search(items, item, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if items[mid] == item:
        return mid
    elif items[mid] > item:
        return binary_search(items, item, start, mid - 1)
    else:
        return binary_search(items, item, mid + 1, end)


def solution_2(item, search):
    result = []
    item.sort()
    for i in search:
        if binary_search(item, i, 0, len(item) - 1):
            result.append("yes")
        else:
            result.append('no')
    return result


def binary_search_2(items, item, start, end):
    while start <= end:
        mid = (start + end) // 2
        if items[mid] > item:
            end = mid - 1
        elif items[mid] < item:
            start = mid + 1
        else:
            return mid


def solution_3(item, search):
    result = []
    item.sort()
    for i in search:
        if binary_search_2(item, i, 0, len(item) - 1):
            result.append("yes")
        else:
            result.append('no')
    return result


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        item = [8, 3, 7, 9, 2]
        search = [5, 7, 9]
        result = solution(item, search)
        self.assertEqual(result, ['no', 'yes', 'yes'])

    def test_something_2(self):
        item = [8, 3, 7, 9, 2]
        search = [5, 7, 9]
        result = solution_2(item, search)
        self.assertEqual(result, ['no', 'yes', 'yes'])

    def test_something_3(self):
        item = [8, 3, 7, 9, 2]
        search = [5, 7, 9]
        result = solution_3(item, search)
        self.assertEqual(result, ['no', 'yes', 'yes'])


if __name__ == '__main__':
    unittest.main()
