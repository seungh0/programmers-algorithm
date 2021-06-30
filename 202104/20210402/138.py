import unittest
from collections import deque


def book_solution(chars: str) -> bool:
    words = []
    for char in chars:
        if char.isalnum():
            words.append(char.lower())
    while len(words) > 1:
        if words.pop() != words.pop(0):
            return False
    return True


def book_fast_solution(chars: str) -> bool:
    words = deque()
    for i in chars:
        if i.isalnum():
            words.append(i.lower())

    while len(words) > 1:
        if words.pop() != words.popleft():
            return False
    return True


def my_solution(words):
    strArray = []
    for word in words:
        if word.isalpha():
            strArray.append(word.lower())
        if word.isdigit():
            strArray.append(word)
    for i in range(len(strArray) // 2):
        if strArray[i] != strArray[len(strArray) - i - 1]:
            return False
    return True


def solution2(words):
    words = ''.join(words.replace(',', '').replace('.', '').replace(':', '').split()).lower()
    for i in range(0, len(words) // 2):
        if words[i] != words[len(words) - i - 1]:
            return False
    return True


def solution3(words):
    strs = deque()

    for char in words:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = my_solution("A man, a plan, a canal: Panama")
        self.assertEqual(result, True)

    def test_something1(self):
        result = my_solution("race a car")
        self.assertEqual(result, False)

    def test_something2(self):
        result = book_solution("A man, a plan, a canal: Panama")
        self.assertEqual(result, True)

    def test_something3(self):
        result = book_solution("race a car")
        self.assertEqual(result, False)

    def test_something4(self):
        result = book_fast_solution("A man, a plan, a canal: Panama")
        self.assertEqual(result, True)

    def test_something5(self):
        result = book_fast_solution("race a car")
        self.assertEqual(result, False)

    def test_something6(self):
        result = solution2("A man, a plan, a canal: Panama")
        self.assertEqual(result, True)

    def test_something7(self):
        result = solution2("race a car")
        self.assertEqual(result, False)

    def test_something8(self):
        result = solution3("A man, a plan, a canal: Panama")
        self.assertEqual(result, True)

    def test_something9(self):
        result = solution3("race a car")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
