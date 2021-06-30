import unittest


def solution(value):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in value:
        if not char in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("()[]{}")
        self.assertEqual(result, True)

    def test_something1(self):
        result = solution("([])")
        self.assertEqual(result, True)

    def test_something2(self):
        result = solution(")")
        self.assertEqual(result, False)

    def test_something3(self):
        result = solution("(")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
