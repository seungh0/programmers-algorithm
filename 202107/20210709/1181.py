import unittest
from collections import defaultdict


def solution(n, words):
    dict = defaultdict(int)
    for word in words:
        dict[word] = len(word)

    arr = []
    for key, value in dict.items():
        arr.append((key, value))

    arr.sort(key=lambda x: (x[1], x[0]))
    return [key for key, value in arr]


n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i in solution(n, words):
    print(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(13, [
            'but',
            'i',
            'wont',
            'hesitate',
            'no',
            'more',
            'no',
            'more',
            'it',
            'cannot',
            'wait',
            'im',
            'yours'
        ])
        self.assertEqual(result, [
            'i',
            'im',
            'it',
            'no',
            'but',
            'more',
            'wait',
            'wont',
            'yours',
            'cannot',
            'hesitate'
        ])


if __name__ == '__main__':
    unittest.main()
