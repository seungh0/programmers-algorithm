import unittest


def solution1(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0
    for i in range(len(gas)):
        if gas[i] + fuel < cost[i]:
            start += 1
            fuel = 0
        else:
            fuel += cost[i] - gas[i]
    return start


def solution(gas, cost):
    for i in range(len(gas)):
        if cost[i] > gas[i]:
            continue

        fuel = 0
        can_travel = False
        for j in range(i, i + len(gas)):
            index = j % len(gas)
            if fuel + gas[index] < cost[index]:
                can_travel = False
                break
            fuel += gas[index] - cost[index]
            can_travel = True
        if can_travel:
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

    def test_something4(self):
        result = solution1([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        self.assertEqual(result, 3)

    def test_something5(self):
        result = solution1([1, 2, 3], [2, 3, 4])
        self.assertEqual(result, -1)

    def test_something6(self):
        result = solution1([1, 2, 3], [2, 3, 1])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
