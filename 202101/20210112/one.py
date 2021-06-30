import unittest


def solution(number, k):
    arr = []
    for i in number:
        arr.append(int(i))

    start = 0
    end = k + 1

    result = ""
    while start < end <= len(number):
        max = start
        for i in range(start, end):
            if arr[max] < arr[i]:
                max = i
        start = max + 1
        end += 1
        result += str(arr[max])
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("1924", 2)
        self.assertEqual(result, "94")

    def test_something2(self):
        result = solution("1231234", 3)
        self.assertEqual(result, "3234")


if __name__ == '__main__':
    unittest.main()
