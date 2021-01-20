import unittest


def fibo_basic(n):
    if n == 1 or n == 2:
        return 1
    return fibo_basic(n - 1) + fibo_basic(n - 2)


### Caching (Memoizatino)
d = [0] * 100


def fibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]


class MyTestCase(unittest.TestCase):
    def test_something2(self):
        result = fibo(5)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
