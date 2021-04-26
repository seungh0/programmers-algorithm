import unittest

phone = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def solution(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        for i in range(index, len(digits)):
            for j in phone[digits[i]]:  # abc
                print(j)
                dfs(i + 1, path + j)

    if not digits:
        return []

    result = []
    dfs(0, "")
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("23")
        self.assertEqual(result, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


if __name__ == '__main__':
    unittest.main()
