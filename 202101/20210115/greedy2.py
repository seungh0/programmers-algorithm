import unittest


def solution(people, limit):
    board = 0
    people.sort(reverse=True)

    left = 0
    right = len(people) - 1

    while left <= right:
        if left == right:
            return board + 1

        if people[left] + people[right] <= limit:
            right -= 1
        left += 1
        board += 1

    return board


class MyTestCase(unittest.TestCase):
    def test_something(self):
        people = [70, 50, 80, 50]
        limit = 100
        result = solution(people, limit)
        self.assertEqual(result, 3)

    def test_something2(self):
        people = [70, 80, 50]
        limit = 100
        result = solution(people, limit)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
