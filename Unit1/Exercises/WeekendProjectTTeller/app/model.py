import os
import json

BASEDIR = os.path.dirname(__file__) # gives the path to the directory containing this file
DATAFILE = "data.json" 
FILEPATH = os.path.join(BASEDIR, DATAFILE) # join containing directory with data file name
                            # to produce full system path to your data file

DATA = {}

def load():
    global DATA
    with open(FILEPATH, "r") as json_file:
        DATA = json.load(json_file)

def save(user_account):
    account_num = user_account["account_num"]
    DATA[account_num] = user_account
    with open(FILEPATH, "w") as json_file:
        json.dump(DATA, json_file, indent=2)

def login(account_num, pin):
    """ TODO: verify pin is correct, raise an exception (maybe KeyError) on bad login """
    return DATA[account_num]

def get_balance(account):
    """ return account's balance """
    pass

def deposit(account, amount):
    """ add amount $ to account's ["balance"] """
    pass

def withdraw(account, amount):
    """ reduce account's ["balance"] by amount, raise ValueError if insufficient funds """
    pass

def new_account(firstname, lastname, pin):
    """ create a new account, generate a random account number, set the values for
    firstname, lastname, and pin. You don't need to save yet.
    return the new account. """
    pass