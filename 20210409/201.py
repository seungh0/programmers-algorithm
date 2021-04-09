import unittest
from collections import deque


def solution(param):
    words = param.split("->")
    return words == words[::-1]


def solution1(param):
    words = param.split("->")
    queue = deque(words)

    while queue:
        if queue.popleft() != queue.pop():
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("1->2")
        self.assertEqual(result, False)

    def test_something1(self):
        result = solution("1->2->2->1")
        self.assertEqual(result, True)

    def test_something2(self):
        result = solution1("1->2")
        self.assertEqual(result, False)

    def test_something3(self):
        result = solution1("1->2->2->1")
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
