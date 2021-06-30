import unittest


def removeZero(n):
    return n.replace("0", ""), n.count('0')


def fibo(n, cnt_zero, cnt_binary):
    # 만약 "1"이면 return
    if n == "1":
        return [cnt_binary, cnt_zero]

    # 모든 0을 제거하고, 0의 갯수를 더한다.
    n, cnt = removeZero(n)
    cnt_zero += cnt

    # 문자열의 길이에 해당하는 이진수로 변경
    n = format(len(n), 'b')
    return fibo(n, cnt_zero, cnt_binary + 1)


def solution(n):
    cnt_zero = 0
    cnt_binary = 0
    return fibo(n, cnt_zero, cnt_binary)


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        result = solution("1")
        self.assertEqual(result, [0, 0])

    def test_something(self):
        result = solution("110010101001")
        self.assertEqual(result, [3, 8])  # 6 -> 7 -> 8
        # 111111 -> 110 -> 11 -> 10 -> 1


if __name__ == '__main__':
    unittest.main()
