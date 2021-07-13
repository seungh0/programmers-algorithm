import unittest

dict = {')': '(', ']': '['}


def solution(word):
    stack = []
    for w in word:
        if w in dict.values():
            stack.append(w)
        elif w in dict.keys():
            if not stack:
                return 'no'
            if stack.pop() != dict[w]:
                return 'no'
    return 'yes' if not stack else 'no'


while True:
    n = input()
    if n == '.':
        break
    print(solution(n))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('So when I die (the [first] I will see in (heaven) is a score list).')
        self.assertEqual(result, 'yes')

    def test_something1(self):
        result = solution('Half Moon tonight (At least it is better than no Moon at all].')
        self.assertEqual(result, 'no')


if __name__ == '__main__':
    unittest.main()
