import unittest
from .exit_miro import solution


class TestSolution(unittest.TestCase):
    def test_solution_case(self):
        # given
        graph = [
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
        ]
        miro_entrance = (0, 0)
        miro_exit = (len(graph) - 1, len(graph[0]) - 1)

        # when
        result = solution(graph, miro_entrance, miro_exit)

        # then
        self.assertEqual(result, 10)

    def test_solution_case_2(self):
        # given
        graph = [
            [1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1]
        ]
        miro_entrance = (0, 0)
        miro_exit = (len(graph) - 1, len(graph[0]) - 1)

        # when
        result = solution(graph, miro_entrance, miro_exit)

        # then
        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()
