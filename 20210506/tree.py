import unittest


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def pre_order(node):
    result = []
    if node is None:
        return result
    result.append(node.data)
    result += pre_order(node.left)
    result += pre_order(node.right)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        root = Node(10)
        root.left = Node(34)
        root.right = Node(89)
        root.left.left = Node(45)
        root.left.right = Node(50)
        self.assertEqual(pre_order(root), [10, 34, 45, 50, 89])


if __name__ == '__main__':
    unittest.main()
