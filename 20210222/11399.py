def solution(n, param):
    param.sort()
    temp = 0
    result = []
    for i in param:
        temp += i
        result.append(temp)
    return sum(result)


if __name__ == '__main__':
    n = int(input())
    r = list(map(int, input().split(" ")))
    print(solution(n, r))
