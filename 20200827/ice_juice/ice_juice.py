def is_out_of_range(graph, x, y):
    return x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0])


def dfs(graph, x, y):
    if is_out_of_range(graph, x, y):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)
        return True
    return False


def solution(graph):
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if dfs(graph, i, j):
                cnt += 1
    return cnt
