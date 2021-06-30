import unittest
from collections import deque


def solution(progresses, speeds):
    answer = []
    days = 0
    queue = deque()
    for progress, speed in zip(progresses, speeds):
        queue.append((progress, speed))

    cnt = 0
    while queue:
        progress, speed = queue[0]
        if progress + speed * days >= 100:
            queue.popleft()
            cnt += 1
            print(days, queue, cnt)
            continue
        else:
            if cnt != 0:
                answer.append(cnt)
            days += 1
            cnt = 0
    # 마지막에 남은거 정리
    answer.append(cnt)
    return answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([93, 30, 55], [1, 30, 5])
        self.assertEqual(result, [2, 1])


if __name__ == '__main__':
    unittest.main()
