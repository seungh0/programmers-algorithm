import unittest


def solution(word):
    def expand(left, right):
        while left >= 0 and right < len(word) and word[left] == word[right]:
            left -= 1
            right += 1
        return word[left + 1: right]

    if len(word) < 2 or word == word[::-1]:
        return word

    result = ''
    for i in range(len(word) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


def solution2(word):
    def expand(start, end):
        while start >= 0 and end < len(word) and word[start] == word[end]:
            start -= 1
            end += 1
        return word[start + 1: end]

    if len(word) < 2 or word == word[::-1]:
        return word
    result = ''
    for i in range(len(word) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('babad')
        self.assertEqual(result, 'bab')

    def test_something2(self):
        result = solution('abba')
        self.assertEqual(result, 'abba')

    def test_something3(self):
        result = solution('a')
        self.assertEqual(result, 'a')

    def test_something4(self):
        result = solution('aab')
        self.assertEqual(result, 'aa')

    def test_something5(self):
        result = solution2('babad')
        self.assertEqual(result, 'bab')

    def test_something6(self):
        result = solution2('abba')
        self.assertEqual(result, 'abba')

    def test_something7(self):
        result = solution2('a')
        self.assertEqual(result, 'a')

    def test_something8(self):
        result = solution2('aab')
        self.assertEqual(result, 'aa')


if __name__ == '__main__':
    unittest.main()
