import unittest


def solution(param):
    param.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    result = []
    for st in param:
        result.append(st[0])
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([
            ('Junkyu', 50, 60, 100),
            ('Sangkeun', 80, 60, 50),
            ('Suyoung', 80, 70, 100),
            ('Soong', 50, 60, 90)
        ])
        self.assertEqual(result, ['Sangkeun', 'Suyoung', 'Junkyu', 'Soong'])


if __name__ == '__main__':
    unittest.main()
