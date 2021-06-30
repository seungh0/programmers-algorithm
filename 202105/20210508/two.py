import unittest

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def init_place(place):
    result = []
    for p in place:
        temp = []
        for word in p:
            temp.append(word)
        result.append(temp)
    return result


def check(place):
    place = init_place(place)
    is_visited = [[False] * len(place) for _ in place]

    def dfs(i, j, cnt):
        if cnt >= 2 or is_visited[i][j]:
            return True
        place[i][j] = '0'
        for x, y in move:
            dx, dy = i + x, j + y
            if dx < 0 or dy < 0 or dx >= len(place) or dy >= len(place[i]):
                continue
            if place[dx][dy] == 'X':
                continue
            if place[dx][dy] == 'P':
                return False
            if not dfs(dx, dy, cnt + 1):
                return False
        return True

    for i in range(len(place)):
        for j in range(len(place[i])):
            if place[i][j] == 'P':
                if not dfs(i, j, 0):
                    return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = check(["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"])
        self.assertEqual(result, 1)

    def test_something2(self):
        result = check(["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"])
        self.assertEqual(result, 0)

    def test(self):
        result = solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                           ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                           ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
        self.assertEqual(result, [1, 0, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
