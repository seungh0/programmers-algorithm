import unittest
import collections

actions = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}


def solution(records):
    people = collections.defaultdict(str)
    queue = collections.deque()
    for record in records:
        spliter = record.split()
        if len(spliter) == 3:
            action, uid, name = record.split()
            people[uid] = name
        else:
            action, uid = record.split()
        queue.append((action, uid))

    answer = []
    while queue:
        action, uid = queue.popleft()
        if action in actions:
            answer.append(people[uid] + actions[action])
    return answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan"
        ])
        self.assertEqual(result, [
            "Prodo님이 들어왔습니다.",
            "Ryan님이 들어왔습니다.",
            "Prodo님이 나갔습니다.",
            "Prodo님이 들어왔습니다."
        ])


if __name__ == '__main__':
    unittest.main()
