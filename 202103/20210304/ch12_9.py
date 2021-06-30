import unittest


def solution(param):
    answer = len(param)
    for i in range(1, len(param) // 2 + 1):
        temp = ""
        cnt = 1
        previous = param[:i]
        for j in range(i, len(param), i):
            if previous == param[j: j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    temp += previous
                else:
                    temp += str(cnt) + previous
                cnt = 1
                previous = param[j: j + i]
        if cnt == 1:
            temp += previous
        else:
            temp += str(cnt) + previous
        answer = min(answer, len(temp))
    return answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("aabbaccc")  # 2a2ba3c
        self.assertEqual(result, 7)

    def test_something1(self):
        result = solution("ababcdcdababcdcd")  # 2ababcdcd
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
