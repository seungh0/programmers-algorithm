import unittest

dict = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solution(s):
    result = ""
    temp = ""
    for word in s:
        if word.isdigit():
            result += word
            continue
        temp += word
        if temp in dict:
            result += str(dict.index(temp))
            temp = ""
    return int(result)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("one4seveneight")
        self.assertEqual(result, 1478)


if __name__ == '__main__':
    unittest.main()
