import unittest


# def solution(enroll, referral, seller, amount):
#     map = {}
#
#     def calc(seller, amount):
#         referral_profits = int(amount * 0.1)
#         if referral_profits < 1:
#             referral_profits = 0
#
#         seller_profits = amount - referral_profits
#         map[seller][1] += seller_profits
#         if map[seller][0] == '-':
#             return
#         calc(map[seller][0], referral_profits)
#
#     for e, r in zip(enroll, referral):
#         map[e] = [r, 0]
#
#     for s, a in zip(seller, amount):
#         calc(s, a * 100)
#     return [i[1] for i in map.values()]


def solution(enroll, referral, seller, amount):
    map = {}

    def calc(seller, price):
        parent_price = 0 if int(price * 0.1) < 1 else int(price * 0.1)
        my_money = price - parent_price
        if map[seller][0] == '-':
            map[seller][1] += my_money
            return
        map[seller][1] += my_money
        calc(map[seller][0], parent_price)

    for e, r in zip(enroll, referral):
        map[e] = [r, 0]

    for s, a in zip(seller, amount):
        calc(s, a * 100)

    return [i[1] for i in map.values()]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                          ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                          ["young", "john", "tod", "emily", "mary"],
                          [12, 4, 2, 5, 10])
        self.assertEqual(result, [360, 958, 108, 0, 450, 18, 180, 1080])


if __name__ == '__main__':
    unittest.main()
