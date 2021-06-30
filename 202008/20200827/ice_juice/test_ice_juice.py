import unittest
from .ice_juice import solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        # given
        graph = [
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]

        # when
        result = solution(graph)

        # then
        self.assertEqual(result, 3)

    def test_solution_case_2(self):
        # given
        graph = [
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0]
        ]

        # when
        result = solution(graph)

        # then
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
