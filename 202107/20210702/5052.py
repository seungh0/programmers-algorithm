import unittest


def solution(test):
    test.sort()
    for i in range(len(test) - 1):
        for j in range(i + 1, len(test)):
            if test[j].startswith(test[i]):
                return 'NO'
    return 'YES'


cnt = int(input())

for _ in range(cnt):
    n = int(input())
    test = []
    for _ in range(n):
        test.append(input())
    print(solution(test))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(['911', '97625999', '91125426'])
        self.assertEqual(result, 'NO')

    def test_something1(self):
        result = solution(['113', '12340', '123440', '12345', '98346'])
        self.assertEqual(result, 'YES')

    def test_startWith(self):
        self.assertTrue("abc".startswith("ab"))


if __name__ == '__main__':
    unittest.main()
