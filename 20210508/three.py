import unittest


def move_up(table, pos, cnt):
    while cnt > 0:
        pos -= 1
        if not table[pos]:
            continue
        cnt -= 1
    return pos if pos > 0 else 0


def move_down(table, pos, cnt):
    if last_pos(table, pos):
        return len(table) - 1
    while cnt > 0:
        pos += 1
        if not table[pos]:
            continue
        cnt -= 1
    return pos


def last_pos(table, pos):
    for i in range(pos, len(table)):
        if table[i]:
            return False
    return True


def calc(table):
    result = ""
    for i in table:
        if i:
            result += 'O'
        else:
            result += 'X'
    return result


def solution(n, k, cmd):
    table = [True for _ in range(n)]
    last_remove = []
    pos = k
    for c in cmd:
        if c.startswith('U'):
            n = int(c.split('U ')[1])
            pos = move_up(table, pos, n)
        if c.startswith('D'):
            n = int(c.split('D ')[1])
            pos = move_down(table, pos, n)
        if c == 'C':
            last_remove.append(pos)
            table[pos] = False
            if last_pos(table, pos):
                pos = move_up(table, pos, 1)
            else:
                pos = move_down(table, pos, 1)
        if c == 'Z':
            table[last_remove.pop()] = True
    return calc(table)


class MyTestCase(unittest.TestCase):
    def test_abcz(self):
        table = [True, False, True, True]
        self.assertEqual(move_down(table, 0, 1), 2)

    def test_abcdz(self):
        table = [True, False, True]
        self.assertEqual(move_up(table, 2, 1), 0)

    def test_something1(self):
        result = solution(8, 2, ["D 2", "C"])
        self.assertEqual(result, "OOOOXOOO")

    def test_something3(self):
        result = solution(8, 2, ["D 2", "C", "U 3"])
        self.assertEqual(result, "OOOOXOOO")

    def test_something4(self):
        result = solution(8, 2, ["D 2", "C", "U 3", "C"])
        self.assertEqual(result, "OXOOXOOO")

    def test_something5(self):
        result = solution(8, 2, ["D 2", "C", "U 3", "C", "D 4"])
        self.assertEqual(result, "OXOOXOOO")

    def test_something6(self):
        result = solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C"])
        self.assertEqual(result, "OXOOXOOX")

    def test_something7(self):
        result = solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2"])
        self.assertEqual(result, "OXOOXOOX")

    def test_something8(self):
        result = solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z"])
        self.assertEqual(result, "OXOOXOOO")

    def test_something2(self):
        result = solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
        self.assertEqual(result, "OOOOXOOO")


if __name__ == '__main__':
    unittest.main()
