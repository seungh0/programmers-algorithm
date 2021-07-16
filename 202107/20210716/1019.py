import unittest


def count_page(count, page):
    while page > 0:
        count[page % 10] += 1
        page = page // 10


def solution(num):
    count = [0] * 10
    for i in range(1, num + 1):
        count_page(count, i)
    return list(map(str, count))


#
# n = int(input())
# print(" ".join(solution(n)))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(11)
        self.assertEqual(result, ['1', '4', '1', '1', '1', '1', '1', '1', '1', '1'])

    def test_something1(self):
        result = solution(1)
        self.assertEqual(result, ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'])


if __name__ == '__main__':
    unittest.main()
