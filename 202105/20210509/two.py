import unittest


def solution(t, r):
    result = []
    number = 0

    waiters = []
    for id, (time, priority) in enumerate(zip(t, r)):
        waiters.append((time, priority, id))
    waiters = sorted(waiters, key=lambda x: (x[1], x[0], x[2]))

    while waiters:
        for waiter in waiters:
            time, priority, id = waiter
            if time <= number:
                waiters.remove(waiter)
                result.append(id)
                break
        number += 1
    return result


# (0, 0), (1, 1), (3, 2), (0, 3)
class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([0, 1, 3, 0], [0, 1, 2, 3])
        self.assertEqual(result, [0, 1, 3, 2])

    def test_something2(self):
        result = solution([7, 6, 8, 1], [0, 1, 2, 3])
        self.assertEqual(result, [3, 1, 0, 2])

    def test_something3(self):
        result = solution([0, 0, 0, 0], [0, 0, 0, 0])
        self.assertEqual(result, [0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
