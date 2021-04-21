import unittest


def solution(needs, cookies):
    needs.sort()
    cookies.sort()

    cnt = 0
    for i, need in enumerate(needs):
        if i >= len(cookies) or need > cookies[i]:
            break
        cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 2, 3], [1, 1])
        self.assertEqual(result, 1)

    def test_something2(self):
        result = solution([1, 2], [1, 2, 3])
        self.assertEqual(result, 2)

    def test_something3(self):
        result = solution([1, 2, 3], [1, 2])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
