import unittest
from bisect import bisect_left, bisect_right


def countMatch(words, left_value, right_value):
    right_index = bisect_right(words, right_value)
    left_index = bisect_left(words, left_value)
    return right_index - left_index


def solution(words, queries):
    result = []
    word_arr = [[] for _ in range(100001)]
    reverse_word_arr = [[] for _ in range(100001)]
    for i in words:
        word_arr[len(i)].append(i)
        reverse_word_arr[len(i)].append(i[::-1])

    for i in range(100001):
        word_arr[i].sort()
        reverse_word_arr[i].sort()

    for query in queries:
        if query[0] != '?':
            result.append(countMatch(word_arr[len(query)], query.replace("?", 'a'), query.replace("?", "z")))
        else:
            r = countMatch(reverse_word_arr[len(query)], query[::-1].replace("?", "a"), query[::-1].replace("?", "z"))
            result.append(r)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(
            ["frodo", "front", "frost", "frozen", "frame", "kakao"],
            ["fro??", "????o", "fr???", "fro???", "pro?"]
        )
        self.assertEqual(result, [3, 2, 4, 1, 0])


if __name__ == '__main__':
    unittest.main()
