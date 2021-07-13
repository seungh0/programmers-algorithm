import unittest


def count_number(result):
    answer = []
    for i in range(0, 10):
        answer.append(str(result).count(str(i)))
    return answer


def solution(param):
    result = 1
    for i in param:
        result *= i
    return count_number(result)


a = int(input())
b = int(input())
c = int(input())

for i in solution([a, b, c]):
    print(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([150, 266, 427])
        self.assertEqual(result, [3, 1, 0, 2, 0, 0, 0, 2, 0, 0])


if __name__ == '__main__':
    unittest.main()
