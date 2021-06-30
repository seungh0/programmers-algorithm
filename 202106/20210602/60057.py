import unittest


def addSentence(comp, cnt):
    if cnt == 1:
        return comp
    return str(cnt) + comp


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        senetences = ""
        comp = ""
        cnt = 1
        for j in range(0, len(s), i):
            temp = s[j:j + i]
            if comp == temp:
                cnt += 1
            else:
                senetences += addSentence(comp, cnt)
                comp = temp
                cnt = 1
        senetences += addSentence(comp, cnt)
        answer = min(answer, len(senetences))
    return answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("aabbaccc")
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
