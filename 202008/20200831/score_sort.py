import unittest


def solution(arr):
    result = sorted(arr, key=lambda student: student[1])
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [('ABC', 95), ('DEF', 90)]
        result = solution(array)
        self.assertEqual(result, [('DEF', 90), ('ABC', 95)])


if __name__ == '__main__':
    unittest.main()
