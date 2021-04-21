import unittest


def solution(gases, costs):
    if sum(gases) < sum(costs):
        return -1

    for i in range(len(gases)):
        own = 0
        for j in range(i, i + len(gases)):
            index = j % len(gases)
            own += (gases[index] - costs[index])
            if own < 0:
                break
        if own >= 0:
            return i
    return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        self.assertEqual(result, 3)

    def test_something2(self):
        result = solution([1, 2, 3], [2, 3, 4])
        self.assertEqual(result, -1)

    def test_something3(self):
        result = solution([1, 2, 3], [2, 3, 1])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
