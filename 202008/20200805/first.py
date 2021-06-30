# 시저함수 (Level 1)
# https://programmers.co.kr/learn/courses/30/lessons/12926
import unittest


def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == " ":
            answer += s[i]
        else:
            answer += calculate(s[i], n)
    return answer


def calculate(value, n):
    temp = ord(value) + n
    if isSmallLetter(value):
        return addSmallLetter(temp)
    elif isBigLetter(value):
        return addBigLetter(temp)
    else:
        raise Exception("A~Z or a-z 사이의 문자만 가능합니다")


def isSmallLetter(letter):
    return (ord(letter) >= 97) & (ord(letter) <= 122)


def isBigLetter(letter):
    return (ord(letter) >= 65) & (ord(letter) <= 90)


def addSmallLetter(letter):
    if letter > 122:
        letter -= 26
    return chr(letter)


def addBigLetter(letter):
    if letter > 90:
        letter -= 26
    return chr(letter)


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        s = "AB"
        n = 1
        # when
        result = solution(s, n)
        # then
        self.assertEqual(result, "BC")

    def test_case2(self):
        # given
        s = "z"
        n = 1
        # when
        result = solution(s, n)
        # then
        self.assertEqual(result, "a")

    def test_case3(self):
        # given
        s = "a B z"
        n = 4
        # when
        result = solution(s, n)
        # then
        self.assertEqual(result, "e F d")

    def test_case4(self):
        # given
        s = "Z"
        n = 1

        # when
        result = solution(s, n)

        # then
        self.assertEqual(result, "A")

    def test_case5(self):
        # given
        s = "["
        n = 1

        # when & then
        with self.assertRaises(Exception):
            solution(s, n)


if __name__ == '__main__':
    unittest.main()
