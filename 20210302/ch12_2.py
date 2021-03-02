import unittest


def solution(param):
    alpha = []
    numbers = []
    for i in param:
        if i.isalpha():
            alpha.append(i)
        else:
            numbers.append(int(i))
    alpha.sort()
    alpha.append(sum(numbers))
    return alpha


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('K1KA5CB7')
        self.assertEqual(result, ['A', 'B', 'C', 'K', 'K', 13])

    def test_something1(self):
        result = solution('AJKDLSI412K4JSJ9D')
        self.assertEqual(result, ['A', 'D', 'D', 'I', 'J', 'J', 'J', 'K', 'K', 'L', "S", "S", 20])


if __name__ == '__main__':
    unittest.main()
