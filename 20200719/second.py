# 전화번호 목록 (Level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42577

import unittest


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        phone_book = ["119", "97674223", "1195524421"]
        # when
        result = solution(phone_book)
        # then
        self.assertFalse(result)

    def test_case2(self):
        # given
        phone_book = ["123", "456", "789"]
        # when
        result = solution(phone_book)
        # then
        self.assertTrue(result)

    def test_case3(self):
        # given
        phone_book = ["12", "123", "1235", "567", "88"]
        # when
        result = solution(phone_book)
        # then
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
