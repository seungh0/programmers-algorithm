from collections import deque

# 동서남북
_directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]


def is_not_road(dx, dy, graph):
    if dx < 0 or dy < 0 or dx >= len(graph) or dy >= len(graph[0]):
        return True
    if graph[dx][dy] != 1:
        return True
    return False


def solution(graph, miro_entrance, miro_exit):
    queue = deque([miro_entrance])
    while queue:
        x, y = queue.popleft()
        for i in range(len(_directions)):
            dx = x + _directions[i][0]
            dy = y + _directions[i][1]
            if is_not_road(dx, dy, graph):
                continue
            graph[dx][dy] = graph[x][y] + 1
            queue.append((dx, dy))
    return graph[miro_exit[0]][miro_exit[1]]
