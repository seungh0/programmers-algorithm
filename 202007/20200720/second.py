# 다리를 지나는 트럭 (Level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42583

import unittest


class Car:
    def __init__(self, weight, exit_second):
        self.weight = weight
        self.exit_second = exit_second

    def canExit(self, second):
        return self.exit_second <= second


class Bridge:
    def __init__(self, bridge_length, bridge_max_weight):
        self.LENGTH = bridge_length
        self.MAX_WEIGHT = bridge_max_weight
        self.bridge_queue = []  # 다리를 건너는 트럭
        self.weight = 0

    def enterBridge(self, car):
        self.bridge_queue.insert(0, car)
        self.__addCarWeight(car)

    def __addCarWeight(self, car):
        self.weight += car.weight

    def exitCarsIfAnyCanExit(self, second):
        idx = len(self.bridge_queue) - 1
        while idx >= 0:
            car = self.bridge_queue[idx]
            if car.canExit(second):
                self.__exitBridge(car)
            idx -= 1

    def __exitBridge(self, car):
        self.bridge_queue.remove(car)
        self.__subtractCarWeight(car)

    def __subtractCarWeight(self, car):
        self.weight -= car.weight

    def canAffordWeight(self, weight):
        return self.MAX_WEIGHT >= self.weight + weight


def solution(bridge_length, weight, truck_weights):
    second = 0  # 경과 시간
    bridge = Bridge(bridge_length, weight)

    while len(truck_weights) > 0:
        second += 1
        bridge.exitCarsIfAnyCanExit(second)

        if bridge.canAffordWeight(truck_weights[0]):
            bridge.enterBridge(Car(truck_weights[0], second + bridge.LENGTH))
            truck_weights.pop(0)

    while len(bridge.bridge_queue) > 0:  # 대기 트럭은 모두 빠졋는데, 다리 Queue 에 남아있는 경우 대응
        second += 1
        bridge.exitCarsIfAnyCanExit(second)

    return second


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        bridge_length = 2
        weight = 10
        truck_weights = [7, 4, 5, 6]
        # when
        result = solution(bridge_length, weight, truck_weights)
        # then
        self.assertEqual(result, 8)

    def test_case2(self):
        # given
        bridge_length = 100
        weight = 100
        truck_weights = [10]
        # when
        result = solution(bridge_length, weight, truck_weights)
        # then
        self.assertEqual(result, 101)

    def test_case3(self):
        # given
        bridge_length = 100
        weight = 100
        truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        # when
        result = solution(bridge_length, weight, truck_weights)
        # then
        self.assertEqual(result, 110)


if __name__ == '__main__':
    unittest.main()
