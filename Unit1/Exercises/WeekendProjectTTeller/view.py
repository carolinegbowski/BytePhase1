
## LOGIN OPTIONS FOR ALL USERS
def print_login_menu():
    """ displays login menu"""
    print("""\nWelcome to Terminal Teller!:                                                       
                                                                                   
    1) Create account                                                              
    2) Log in                                                                      
    3) Quit                                                                        
""")

def login_menu_prompt():
    """ prompts user to input choice from login menu"""
    return input("Your choice: ")

## IF QUIT

#       EXITING 
def goodbye():
    """ if user quits, prints goodbye""" 
    print("\n    Goodbye!\n")

## IF LOG IN 

#       GATHERING LOGIN DATA
def login_account_num():
    """ if user logs in, gathers account number from user"""
    return input("\nAccount Number: ")
def login_pin():
    """ if user logs in, gathers pin from user"""
    return input("PIN: ")

#       IF BAD LOGIN
def bad_login_input():
    """ if bad login, tells user that login not recognized"""
    print("Input not recognized. Please try again.\n")
def bad_account_login():
    print("\nInvalid account number or password. Please try again!")


#       IF SUCCESSFUL LOGIN
def print_main_menu(account):
    """ if user successfully logs in, prints main menu options"""
    print(f"""
    Hello, {account["first"]} {account["last"]} ({account["account_num"]})                                                    
                                                                                
    1 Check balance                                                       
    2 Withdraw funds                                                           
    3 Deposit funds                                                            
    4 Sign out
""")

def main_prompt():
    """ when user logged in, prompts input for main menu options"""
    return input("Your choice: ")

## IF CHOOSE CREATE ACCOUNT 

#       GATHERING ACCOUNT DATA
def new_account_creation():
    """ prints instructions for new account creation"""
    print("\nAccount Creation\nEnter the following information to create your account.\n")
def first_name():
    """ gets first name from new customer"""
    return input("First Name: ")
def last_name():
    """ gets last name from new customer"""
    return input("Last Name: ")
def initial_balance():
    return input("How much would you like to deposit?: $")
def pin():
    """ gets PIN from new customer"""
    return input("4 digit PIN: ")
def confirm_pin():
    """ confirms pin from new customer"""
    return input("Confirm PIN: ")
def new_account_number(new_account_number):
    return print("\nAccount Created\nYour new account number is: " + str(new_account_number)+ "\n")

#       IF PINS DONT MATCH 
def pin_not_confirmed():
    print("\nPINs did not match. Please try again\n")


#### MAIN MENU OPTIONS
# if user chooses withdraw
def enter_withdraw_info():
    return input("\nWithdraw Funds\nHow much to withdraw?: $")
def insufficient_funds():
    print("\n!! INSUFFICIENT FUNDS !! YOU'RE POOR !!")
def enter_deposit_info():
    return input("\nDeposit Funds\nHow much to deposit?: $")
def give_balance(balance):
    print("\nYour balance is: ${:.2f}\n".format(balance))