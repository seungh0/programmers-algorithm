import unittest


def solution(nodes):
    nodes = nodes.split(", ")
    result = []
    for node in nodes:
        result += node.split("->")
    result.sort()
    return '->'.join(result)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("1->2->4, 1->3->4")
        self.assertEqual(result, "1->1->2->3->4->4")


if __name__ == '__main__':
    unittest.main()
