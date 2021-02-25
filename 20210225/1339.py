import unittest


def solution(param):
    q = []
    for i in range(len(param)):
        length = len(param[i])
        for j in range(len(param[i])):
            q.append((param[i][j], length - j))

    q = sorted(q, key=lambda x: x[1], reverse=True)

    storage = [0 for _ in range(10)]

    now = 9
    while q:
        word, digit = q.pop(0)
        i = ord(word) - ord('A')
        if storage[i] == 0:
            storage[i] = now
            now -= 1

    result = 0
    for i in range(len(param)):
        length = len(param[i])
        for j in range(len(param[i])):
            r = storage[ord(param[i][j]) - ord('A')]
            result += r * 10 ** ((length - j) - 1)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(['AAA', 'AAA'])
        self.assertEqual(result, 1998)

    def test_something1(self):
        result = solution(['GCF', 'ACDEB'])
        self.assertEqual(result, 99437)

    def test_something2(self):
        result = solution(['AB', 'BA'])
        self.assertEqual(result, 187)


if __name__ == '__main__':
    unittest.main()
