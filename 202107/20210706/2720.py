import unittest

coins = [25, 10, 5, 1]


def solution(money):
    answer = [0] * len(coins)
    for i, coin in enumerate(coins):
        cnt = money // coin
        money -= coin * cnt
        answer[i] = cnt
    return answer

n = int(input())
for _ in range(n):
    result = solution(int(input()))
    for i in result:
        print(i, end=" ")
    print()

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(124)
        self.assertEqual(result, [4, 2, 0, 4])


if __name__ == '__main__':
    unittest.main()
