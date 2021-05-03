import unittest


def is_same_start_with(a, b):
    if a.startswith(b) | b.startswith(a):
        return True
    return False


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if is_same_start_with(phone_book[i], phone_book[i + 1]):
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(["119", "97674223", "1195524421"])
        self.assertFalse(result)

    def test_something1(self):
        result = solution(["123", "456", "789"])
        self.assertTrue(result)

    def test_something2(self):
        result = solution(["12", "123", "1235", "567", "88"])
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
