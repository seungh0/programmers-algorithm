import unittest


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preOrder(trees, node):
    answer = [node.data]
    if node.left != '.':
        answer += preOrder(trees, trees[node.left])
    if node.right != '.':
        answer += preOrder(trees, trees[node.right])
    return answer


def postOrder(trees, node):
    answer = []
    if node.left != '.':
        answer += postOrder(trees, trees[node.left])
    if node.right != '.':
        answer += postOrder(trees, trees[node.right])
    answer.append(node.data)
    return answer


def inOrder(trees, node):
    answer = []
    if node.left != '.':
        answer += inOrder(trees, trees[node.left])
    answer.append(node.data)
    if node.right != '.':
        answer += inOrder(trees, trees[node.right])
    return answer


def solution(n, nodes):
    trees = {}
    for node, left, right in nodes:
        trees[node] = Node(node, left, right)

    root = trees['A']
    return [preOrder(trees, root), inOrder(trees, root), postOrder(trees, root)]


n = int(input())
nodes = []
for _ in range(n):
    nodes.append(input().split())
result = solution(n, nodes)
for r in result:
    for j in r:
        print(j, end='')
    print()


class MyTestaCase(unittest.TestCase):
    def test_something(self):
        result = solution(7, [
            ['A', 'B', 'C'],
            ['B', 'D', '.'],
            ['C', 'E', 'F'],
            ['E', '.', '.'],
            ['F', '.', 'G'],
            ['D', '.', '.'],
            ['G', '.', '.']
        ])
        self.assertEqual(result, [
            ['A', 'B', 'D', 'C', 'E', 'F', 'G'],
            ['D', 'B', 'A', 'E', 'C', 'F', 'G'],
            ['D', 'B', 'E', 'G', 'F', 'C', 'A']
        ])


if __name__ == '__main__':
    unittest.main()
