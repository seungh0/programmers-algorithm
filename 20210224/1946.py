import sys

input = sys.stdin.readline


def solution(info):
    info.sort()
    people = sorted(info, key=lambda x: x[0])
    cnt = 0
    prev = 1e9
    for i in people:
        if i[1] < prev:
            cnt += 1
            prev = i[1]
    return cnt


t = int(input())

for i in range(t):
    n = int(input())
    rank = []
    for i in range(n):
        a, b = map(int, input().split(" "))
        rank.append((a, b))
    print(solution(rank))
