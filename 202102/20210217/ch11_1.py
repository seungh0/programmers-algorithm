import unittest


def solution(n, people):
    result = 0
    people.sort()
    cnt = 0
    for i in people:
        cnt += 1
        if cnt >= i:
            result += 1
            cnt = 0
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 5
        people = [2, 3, 1, 2, 2]
        result = solution(n, people)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
