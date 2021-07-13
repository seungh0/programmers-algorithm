import unittest


def solution(words):
    answer = []
    for word in words.split(" "):
        answer.append(word.lower().capitalize())
    return ' '.join(answer)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("3people unFollowed me")
        self.assertEqual(result, "3people Unfollowed Me")

    def test_something1(self):
        result = solution("for the last week")
        self.assertEqual(result, "For The Last Week")

    def test_something2(self):
        result = solution("333 333 333")
        self.assertEqual(result, "333 333 333")


if __name__ == '__main__':
    unittest.main()
