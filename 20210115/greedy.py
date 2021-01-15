import unittest


def solution(n, l, r):
    lost = list(set(l) - set(r))
    reserve = list(set(r) - set(l))

    cnt = n - len(lost)

    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            cnt += 1

    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            cnt += 1
            continue
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            cnt += 1
            continue

    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        lost = [2, 4]
        reserve = [1, 3, 5]
        result = solution(5, lost, reserve)
        self.assertEqual(result, 5)

    def test_2(self):
        lost = [2, 4]
        reserve = [3]
        result = solution(5, lost, reserve)
        self.assertEqual(result, 4)

    def test_3(self):
        lost = [1, 2]
        reserve = [2, 3]
        result = solution(3, lost, reserve)
        self.assertEqual(result, 2)

    def test_4(self):
        lost = [2, 3]
        reserve = [1, 2]
        result = solution(2, lost, reserve)
        self.assertEqual(result, 1)

    def test_5(self):
        lost = [1, 2, 3, 4]
        reserve = [1, 2, 3, 4]
        result = solution(4, lost, reserve)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
