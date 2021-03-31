import unittest


def solution(n, money, coins):
    coins.sort(reverse=True)
    answer = 0
    i = 0
    while money >= 0 and i < len(coins):
        cnt = money // coins[i]
        money -= cnt * coins[i]
        answer += cnt
        i += 1
    return answer


n, money = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
print(solution(n, money, coins))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(10, 4200, [1, 5, 10, 50, 100, 500, 1000, 5000, 100000, 50000])
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
