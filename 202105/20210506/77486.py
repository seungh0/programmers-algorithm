import unittest


def solution(enroll, referral, seller, amount):
    name_zip = {}

    def calc(seller, price):
        referral_profits = 0 if int(price * 0.1) < 1 else int(price * 0.1)
        my_profits = price - referral_profits
        name_zip[seller][1] += my_profits
        if name_zip[seller][0] == '':
            return
        calc(name_zip[seller][0], referral_profits)

    for e, r in zip(enroll, referral):
        name_zip[e] = ['', 0]
        name_zip[e][0] = r if r != '-' else ''

    for s, a in zip(seller, amount):
        price = a * 100
        calc(s, price)
    return [i[1][1] for i in name_zip.items()]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
        referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
        seller = ["young", "john", "tod", "emily", "mary"]
        amount = [12, 4, 2, 5, 10]
        result = solution(enroll, referral, seller, amount)
        self.assertEqual(result, [360, 958, 108, 0, 450, 18, 180, 1080])


if __name__ == '__main__':
    unittest.main()
