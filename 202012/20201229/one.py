import unittest


class Position:
    def __init__(self, size):
        self.x = 1
        self.y = 1
        self.size = size

    def move(self, direction):
        if direction == "U":
            if self.x <= 1:
                return
            self.x -= 1
        elif direction == 'D':
            if self.x >= self.size:
                return
            self.x += 1
        elif direction == 'L':
            if self.y <= 1:
                return
            self.y -= 1
        elif direction == 'R':
            if self.y >= self.size:
                return
            self.y += 1
        else:
            raise Exception("잘못된 방향입니다")

    def getPos(self):
        return self.x, self.y


def solution(size, moves):
    pos = Position(size)
    for i in moves:
        pos.move(i)
    return pos.getPos()


class TestCase(unittest.TestCase):
    def test_case_1(self):
        result = solution(5, ['R', 'R', 'R', 'U', 'D', 'D'])
        self.assertEqual(result, (3, 4))
