import unittest


def separate(i):
    def split(word):
        return word.split("=")[1]

    price, c, time = i.split()
    price, c, time = split(price), split(c), split(time)
    return price, c, time


def findData(code, day, data):
    result = []
    for i in data:
        price, c, time = separate(i)
        if code != c:
            continue
        if day != time[:8]:
            continue
        result.append(i)
    return result


def solution(code, day, data):
    result = findData(code, day, data)
    result.sort(key=lambda x: x.split()[2].split("=")[1])
    return [int(r.split()[0].split("=")[1]) for r in result]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("012345", "20190620",
                          ["price=80 code=987654 time=2019062113", "price=90 code=012345 time=2019062014",
                           "price=120 code=987654 time=2019062010", "price=110 code=012345 time=2019062009",
                           "price=95 code=012345 time=2019062111"])
        self.assertEqual(result, [110, 90])


if __name__ == '__main__':
    unittest.main()
