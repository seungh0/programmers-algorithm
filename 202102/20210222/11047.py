def solution(price, coins):
    coins.sort(reverse=True)
    cnt = 0
    i = 0
    while price > 0:
        tmp = price // coins[i]
        cnt += tmp
        price -= tmp * coins[i]
        i += 1
    return cnt


if __name__ == '__main__':
    n, price = map(int, input().split(" "))
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    solution(price, coins)
