import unittest


def solution(s):
    s = s.lower()
    cnt_p = 0
    cnt_y = 0
    for i in s:
        if i == 'p':
            cnt_p += 1
        if i == 'y':
            cnt_y += 1
    return cnt_y == cnt_p


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('pPoooyY')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
