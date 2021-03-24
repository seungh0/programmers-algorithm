import unittest


def find_max(start, end, numbers):
    max_index = start
    for i in range(start, end + 1):
        if numbers[i] == 9:
            return i
        if numbers[max_index] < numbers[i]:
            max_index = i
    return max_index


def solution(number, k):
    k = len(number) - k
    number = [int(i) for i in number]
    start = 0
    end = len(number) - k
    result = ""
    for i in range(k):
        m = find_max(start, end, number)
        result += str(number[m])
        start = m + 1
        end += 1
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("1924", 2)
        self.assertEqual(result, "94")

    def test_something1(self):
        result = solution("1231234", 3)
        self.assertEqual(result, "3234")

    def test_something2(self):
        result = solution("4177252841", 4)
        self.assertEqual(result, "775841")


if __name__ == '__main__':
    unittest.main()
