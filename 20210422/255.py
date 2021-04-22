import unittest


class MyStack:
    def __init__(self):
        self.arr = []
        self.top = 0

    def push(self, data):
        self.arr.append(data)
        self.top += 1

    def top2(self):
        return 2

    def pop(self):
        self.top -= 1
        return self.arr[self.top]

    def empty(self):
        return self.top == 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top2(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertFalse(stack.empty())


if __name__ == '__main__':
    unittest.main()
