
import os
import json
from random import randint

BASEDIR = os.path.dirname(__file__) # gives the path to the directory containing this file
DATAFILE = "data.json" 
FILEPATH = os.path.join(BASEDIR, DATAFILE) # join containing directory with data file name
                            # to produce full system path to your data file

class LoginError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass
# controller can then raise these specific errors with try / except
# if your balance is too low, we can signal insufficient funds error etc. 


class Model: 

    datafile = FILEPATH

    def __init__(self, **kwargs):
        """ Constructor // Initializer """
        self.account_num = kwargs.get("account_num")
        self.first = kwargs.get("first")
        self.last = kwargs.get("last")
        self.balance = kwargs.get("balance")
        self.pin = kwargs.get("pin")
    
    def update(self, **kwargs):
        """ updates account info. If only given 2 values, updates only those and keeps the rest"""
        self.account_num = kwargs.get("account_num", self.account_num) 
        self.first = kwargs.get("first", self.first)
        self.last = kwargs.get("self", self.last)
        self.balance = kwargs.get("balance", self.balance)
        self.pin = kwargs.get("pin", self.pin)
        return 

    def save(self):
        """ saves user account, but if account num doesnt exist, gives a new account num """
        if self.account_num == None: 
            self.account_num = randint(100000,999999)
    
        with open(self.datafile, "r") as json_file:
            data = json.load(json_file)
        
        new_data = {}
        new_data["account_num"] = self.account_num
        new_data["first"] = self.first
        new_data["last"] = self.last
        new_data["balance"] = round(float(self.balance), 2)
        new_data["pin"] = self.pin

        account_num = self.account_num
        data[account_num] = new_data

        with open(self.datafile, "w") as json_file:
            json.dump(data, json_file, indent=2)

        return account_num
    
    def login(self, account, pin):
        """ Gets account data for user when correct account num & pin are entered """
        with open(self.datafile, "r") as json_file:
            data = json.load(json_file)

        if (data.get(account) != None) and (data[account]["pin"] == pin):
            self.set_from_dictionary(data[account])
            return data[account]
        else:
            return None
    
    def set_from_dictionary(self, dictionary):
        """ """
        self.first = dictionary.get("first")
        self.last = dictionary.get("last")
        self.balance = dictionary.get("balance")
        self.account_num = dictionary.get("account_num")
        self.pin = dictionary.get("pin")

    def get_balance(self, account):
        """ shows logged in user their account balance"""
        return account["balance"]

    def deposit(self, account, amount):
        """ deposits desired amount to user's account balance""" 
        account["balance"] = account["balance"] + amount
        self.update(balance=account["balance"])
        self.save()
        return 
    
    def withdraw(self, account, amount):
        """ withdraws desired amount from user's account balance""" 
        """ TODO: raise ValueError if insufficient funds """
        if amount > account["balance"]:
            return 0
        account["balance"] = account["balance"] - amount
        self.update(balance=account["balance"])
        self.save()
        return
