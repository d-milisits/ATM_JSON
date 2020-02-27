from model import Account
import unittest

class TestModel(unittest.TestCase):

    def test_constructor(self):
        dan = Account("4221","333409",0)
        self.assertEqual(dan.pin, "4221")
        self.assertEqual(dan.account_num, "333409")
        self.assertEqual(dan.balance, 0)

    # def test_self(self):
    #     dan = Account("4221","333409",0)
    #     self.assertTupleEqual(dan.info(333409))

    def test_deposit(self):
        dan = Account("4221","333409",0)
        dan.deposit(1000)
        self.assertEqual(dan.balance, 1000)

        self.assertRaises(ValueError,dan.deposit,-2000)
        self.assertRaises(ValueError,dan.deposit,0)

    def test_withdraw(self):
        dan = Account("4221","333409",0)
        self.assertRaises(ValueError,dan.withdraw,1000)
    
    def test_view_info(self):
        dan = Account("4221","333409",0)
        result = dan.view_info()
        self.assertEqual(result, "\n***Your current balance in account #{} is: ${}.***\n".format(dan.account_num,dan.balance))

