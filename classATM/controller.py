import view
import sys
from random import randint
from model import Account

def atm():
    view.main_menu()
    selection=view.option_prompt()
    if selection=="1":
        x=str(randint(100000,500000))
        random_num=x
        new_pin=view.create_pin()
        acc=Account(str(new_pin),x)
        view.new_account_success()
        atm()
    if selection=="2":
        acc=view.acc_num_prompt()
        if Account.validate(acc):
            info=Account.info(acc)
            account=Account(info[0],acc,info[1])
            selection=view.option_prompt()
            if selection=="1":
                amount=view.specify_amount()
                account.withdraw(int(amount))
                atm()
            elif selection=="2":
                amount=view.specify_amount()
                account.deposit(int(amount))
                atm()
            elif selection=="3":
                account.view_info()
                atm()
    if selection=="3":
        view.exit()
atm()


