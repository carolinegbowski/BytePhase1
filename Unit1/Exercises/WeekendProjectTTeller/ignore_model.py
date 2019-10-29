
import os
import json
from random import randint

BASEDIR = os.path.dirname(__file__) # gives the path to the directory containing this file
DATAFILE = "data.json" 
FILEPATH = os.path.join(BASEDIR, DATAFILE) # join containing directory with data file name
                            # to produce full system path to your data file

DATA = {}

def load():
    """ loads json """
    global DATA
    with open(FILEPATH, "r") as json_file:
        DATA = json.load(json_file)

def save(user_account):
    """ saves to json """ 
    account_num = user_account["account_num"]
    account_num = str(account_num)
    DATA[account_num] = user_account
    with open(FILEPATH, "w") as json_file:
        json.dump(DATA, json_file, indent=2)

### IF USER CHOSE LOG IN 
def login(account, pin):
    """ logs in user"""
    if DATA[account]["pin"] == pin:
        return DATA[account]
    else:
        pass
    """ TODO: verify pin is correct, raise an exception (maybe KeyError) on bad login """

def get_balance(account):
    """ shows logged in user their account balance"""
    """ return account's balance """
    return account["balance"]

def deposit(account, amount):
    """ deposits desired amount to user's account balance""" 
    """ add amount $ to account's ["balance"] """
    account["balance"] = account["balance"] + amount
    save(account)
    return 

def withdraw(account, amount):
    """ withdraws desired amount from user's account balance""" 
    """ reduce account's ["balance"] by amount, raise ValueError if insufficient funds """
    if amount > account["balance"]:
        return 0
    account["balance"] = account["balance"] - amount
    save(account)
    return

### IF USER CHOSE CREATE ACCOUNT
def new_account(first_name, last_name, pin):
    """ create's new account for new user""" 
    new_account_number = randint(100000,999999)
    new_account_data = {}
    new_account_data["first"] = first_name
    new_account_data["last"] = last_name
    new_account_data["balance"] = round(0, 2)
    new_account_data["account_num"] = new_account_number
    new_account_data["pin"] = pin
    save(new_account_data)
    """ create a new account, generate a random account number, set the values for
    firstname, lastname, and pin. You don't need to save yet.
    return the new account. """
    return new_account_number