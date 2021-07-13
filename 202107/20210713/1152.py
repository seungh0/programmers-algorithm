import unittest


def solution(param):
    return len(param.split())

n = input()
print(solution(n))

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('The Curious Case of Benjamin Button')
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
