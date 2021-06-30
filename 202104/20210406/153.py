import unittest
import collections


def solution(words):
    word_dict = collections.defaultdict(list)
    for word in words:
        keyword = ''.join(sorted(word))
        word_dict[keyword].append(word)

    for word in word_dict:
        word_dict[word].sort()

    return list(word_dict.values())


def solution2(words):
    word_dict = collections.defaultdict(list)
    for word in words:
        word_dict[''.join(sorted(word))].append(word)

    for word in word_dict:
        word_dict[word].sort()

    return list(word_dict.values())


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(result, [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ])

    def test_something2(self):
        result = solution2(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(result, [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ])


if __name__ == '__main__':
    unittest.main()
