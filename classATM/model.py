import json
import os 
import view

DIR = os.path.dirname(__file__)
DATAFILENAME = "accounts.json"
DATAPATH = os.path.join(DIR,DATAFILENAME)

class Account:
    data_path = DATAPATH
    # pin_list=[]

    def __init__(self,pin="",account_num="",balance=0):
        self.pin=pin
        self.account_num=account_num
        self.balance=balance
        self.save()
        # Account.pin_list.append(self.pin)

    def save(self):
        with open(self.data_path,"r") as json_file:
            account_data = json.load(json_file)
            account_data[self.account_num] = {"Pin":self.pin,"Balance":self.balance}
        with open(self.data_path,"w") as json_file:
            json.dump(account_data,json_file,indent=4)
        
    def num_check(accnum):
        with open(Account.data_path,"r") as json_file:
            account_data = json.load(json_file)
            if accnum not in account_data:
                return False
            else:
                return True
    
    # def pin_check(pin):
    #     with open(Account.data_path,"r") as json_file:
    #         account_data = json.load(json_file)
    #         if accnum not in account_data["Pin"]:
    #             return False
    #         else: return True 
    
    def validate(acc):
        if Account.num_check(acc):
            view.user_options()
            return True
        else:
            view.pin_error()
            Account.validate(acc)

    def info(accountNum):
        with open(Account.data_path,"r") as json_file:
            account_data=json.load(json_file)
            pin=account_data[accountNum]["Pin"]
            balance=account_data[accountNum]["Balance"]
            return pin,balance
    
    #take in pin, check if pin in json, if it does, use that information 
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount  
            self.save()
            print("\nYou have deposited ${}.\n".format(amount))       
        else:
            raise ValueError
    
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError
        else:
            self.balance-=amount
            self.save()
            print("\nYou have decided to withdraw ${}.".format(amount))
        
    def view_info(self):
        print("\n***Your current balance in account #{} is: ${}.***\n".format(self.account_num,self.balance))
    