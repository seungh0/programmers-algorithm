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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        item = [8, 3, 7, 9, 2]
        search = [5, 7, 9]
        result = solution(item, search)
        self.assertEqual(result, ['no', 'yes', 'yes'])


if __name__ == '__main__':
    unittest.main()
