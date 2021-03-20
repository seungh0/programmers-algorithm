import unittest


def solution(n, param):
    answer = []
    length = len(param)

    for i in range(1, n + 1):
        count = param.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        result = solution(4, [4, 4, 4, 4, 4])
        self.assertEqual(result, [4, 1, 2, 3])

    def test_something2(self):
        result = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
        self.assertEqual(result, [3, 4, 2, 1, 5])


if __name__ == '__main__':
    unittest.main()
