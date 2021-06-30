import unittest
import collections


# def solution(people, limit):
#     people.sort(reverse=True)
#     deque = collections.deque(people)
#
#     cnt = 0
#     while deque:
#         max_weight = deque.popleft()
#         for person in deque:
#             if max_weight + person <= limit:
#                 deque.remove(person)
#                 if not deque:
#                     break
#         cnt += 1
#     return cnt


def solution(people, limit):
    people.sort(reverse=True)
    deque = collections.deque(people)

    cnt = 0
    while deque:
        if len(deque) == 1:
            cnt += 1
            break
        max_weight = deque.popleft()
        if max_weight + deque[-1] <= limit:
            deque.pop()
        cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([70, 50, 80, 50], 100)
        self.assertEqual(result, 3)

    def test_something1(self):
        result = solution([70, 50, 80], 100)
        self.assertEqual(result, 3)

    def test_something2(self):
        result = solution([50, 50], 100)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
