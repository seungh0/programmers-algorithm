import unittest


def init_array(n, m, params):
    one = []
    two = []
    for i in range(n):
        one.append(params[i])
    for i in range(n, len(params)):
        two.append(params[i])
    return one, two


def solution(n, m, params):
    one, two = init_array(n, m, params)
    result = []
    for i in one:
        if i in two:
            result.append(i)
    return len(result), sorted(result)


n, m = map(int, input().split())
result = []
for i in range(n + m):
    result.append(input())
print(solution(n, m, result))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(3, 4, [
            'ohhenrie',
            'charlie',
            'baesangwook',
            'obama',
            'baesangwook',
            'ohhenrie',
            'clinton'
        ])
        self.assertEqual(result, (2, ['baesangwook', 'ohhenrie']))


if __name__ == '__main__':
    unittest.main()
