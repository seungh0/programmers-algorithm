import unittest


def solution(s):
    answer = []
    for i in s:
        if not answer:
            answer.append(i)
        else:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)
    return not answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("baabaa")
        self.assertEqual(result, 1)

    def test_something1(self):
        result = solution("cdcd")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
