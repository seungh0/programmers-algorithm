import unittest
import collections
import re


def solution(words, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', words)
        .lower()
        .split()
             if word not in banned]
    strArray = collections.defaultdict(int)
    for word in words:
        strArray[word] += 1
    return max(strArray, key=strArray.get)


def solution1(words, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', words).lower().split()
             if word not in banned]
    return collections.Counter(words).most_common(1)[0][0]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
        self.assertEqual(result, "ball")

    def test_something1(self):
        result = solution1("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
        self.assertEqual(result, "ball")


if __name__ == '__main__':
    unittest.main()
