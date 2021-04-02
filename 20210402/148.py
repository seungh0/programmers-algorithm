import unittest


def solution(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1], x.split()[0]))
    return letters + digits


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
        self.assertEqual(result, ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"])


if __name__ == '__main__':
    unittest.main()
