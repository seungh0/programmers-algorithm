import unittest


def solution(people):
    people.sort()
    result = 0
    count = 0
    for i in people:
        count += 1
        if count >= i:
            result += 1
            count = 0
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        man = [2, 3, 1, 2, 2]
        result = solution(man)
        self.assertEqual(result, 2)

    def test_something2(self):
        man = [5, 3, 1, 2, 2]
        result = solution(man)
        self.assertEqual(result, 2)

    def test_something3(self):
        man = [6, 1, 1, 1, 1]
        result = solution(man)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
