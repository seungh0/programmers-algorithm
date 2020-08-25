from .Point import Point


def solution(pos):
    x = int(ord(pos[0])) - int(ord('a')) + 1
    y = int(pos[1])
    point = Point(x, y, 8)

    steps = [
        (-2, -1), (-2, 1), (-1, 2), (-1, -2),
        (1, 2), (1, -2), (2, 1), (2, -1)
    ]

    cnt = 0
    for step in steps:
        if point.can_move(step[0], step[1]):
            cnt += 1
    return cnt
