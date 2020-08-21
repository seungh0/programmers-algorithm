import unittest


class Point:
    def __init__(self, size, x=1, y=1):
        self.x = x
        self.y = y
        self.size = size

    def move(self, i):
        if i == "R":
            self.move_y(1)
        if i == "L":
            self.move_y(-1)
        if i == "U":
            self.move_x(-1)
        if i == "D":
            self.move_x(1)

    def move_x(self, distance):
        if self.x + distance < 1 or self.x + distance > self.size:
            return
        self.x += distance

    def move_y(self, distance):
        if self.y + distance < 1 or self.y + distance > self.size:
            return
        self.y += distance


def solution(n, plan):
    point = Point(n)
    for i in plan:
        point.move(i)
    return [point.x, point.y]


def solution_book(n, plans):
    x, y = 1, 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    return [x, y]


class MyTestCase(unittest.TestCase):
    def test_solution_case_1(self):
        n = 5
        plan = ['R', 'R', 'R', 'U', 'D', 'D']
        result = solution(n, plan)
        self.assertEqual(result, [3, 4])

    def test_solution_case_2(self):
        n = 5
        plan = ['R', 'R', 'R', 'U', 'D', 'D']
        result = solution_book(n, plan)
        self.assertEqual(result, [3, 4])


if __name__ == '__main__':
    unittest.main()
