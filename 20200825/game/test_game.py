# 게임 개발 테스트 코드

import unittest
from .main import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # given
        size = [4, 4]
        start = [1, 1, 0]
        location = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]

        # when
        result = solution(size, start, location)

        # then
        self.assertEqual(result, 3)

    def test_something_2(self):
        # given
        size = [3, 3]
        start = [1, 1, 0]
        location = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1]
        ]

        # when
        result = solution(size, start, location)

        # then
        self.assertEqual(result, 2)

    def test_something_3(self):
        # given
        size = [2, 2]
        start = [1, 1, 0]
        location = [
            [0, 0],
            [0, 0],
        ]

        # when
        result = solution(size, start, location)

        # then
        self.assertEqual(result, 4)

    def test_something_4(self):
        # given
        size = [3, 4]
        start = [1, 1, 0]
        location = [
            [1, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 0]
        ]

        # when
        result = solution(size, start, location)

        # then
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
