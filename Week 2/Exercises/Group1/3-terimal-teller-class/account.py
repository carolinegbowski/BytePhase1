import json
import os

BASEDIR = os.path.dirname(__file__)
DEFAULT_FILENAME = "data.json"
DATAPATH = os.path.join(BASEDIR, DEFAULT_FILENAME)

# define your own error InsufficientFundsError

class Account:
    data_path = DATAPATH

    def __init__(self, **kwargs):
        self.account_num = kwargs.get("account_num")
        # etc.
        # set parameters from keyword arguments
        pass

    def save(self):
        # if self.account_num is not set, create random account_num
        # write entry into data_path
        pass

    @classmethod
    def login(cls, account_num, pin):
        # Return new Account object with correct properties set if account_num
        # exists and has pin=pin. return None otherwise.
        pass

    @classmethod
    def from_account_num(cls, account_num):
        # Return new Account object with correct properties if account_num
        # exists. None otherwise.
        pass
    
    def deposit(self, amount):
        # add amount to self.balance, raise ValueError if amount is < 0
        pass

    def withdraw(self, amount):
        # remove amount from self.balance, raise ValueErrror if amount is < 0
        pass  
    
    def __repr__(self, amount):
        # return string 
        return super().__repr__()
