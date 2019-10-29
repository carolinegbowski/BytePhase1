import view
import model
# or from . import view


def run():
    model.load()    
    while True:
        user_account = login_menu()  # returns the logged in user or None for quit
        if user_account == None:  # login menu returns None if 'quit' is selected
            break
        else:
            main_menu(user_account)  # when the user exits the main menu they will go back to login

def login_menu():
    while True:
        view.print_login_menu()
        choice = view.login_menu_prompt().strip()
        if choice not in ("1", "2", "3"):
            view.bad_login_input()
            return login_menu()
        elif choice == "3":
            view.goodbye()
            return None # return None for quit

        elif choice == "1":
            create_account()
            """ TODO: prompt for firstname, lastname, and pin, and confirm pin
            create the account and then tell the user what their new account number is """

        elif choice == "2":
            """ TODO: prompt functions to ask for account and PIN, use try, except
            to check for bad login """
            account = view.login_account_num()
            pin = view.login_pin()
            account_data = model.login(account, pin)
            return main_menu(account_data)

def create_account():
    """ called from main menu if user chooses create account"""
    """ call this from the main login loop """
    view.new_account_creation()
    first_name = view.first_name()
    last_name = view.last_name()
    pin = view.pin()
    confirmed_pin = view.confirm_pin()
    if pin == confirmed_pin:
        new_account_number = model.new_account(first_name, last_name, pin)
        view.new_account_number(new_account_number)   #should show the account number to the user 
    else: 
        return


# def login_attempt(account, pin):
#     return model.login(account, pin)
#     """ call this from the main login loop """
#     """ called from main menu if user chooses login"""

def main_menu(user):
    while True:
        view.print_main_menu(user)
        choice = view.main_prompt()
        """ TODO: add bad input message """
        if choice not in ("1", "2", "3", "4"):
            view.bad_login_input()
            return main_menu(user)
        if choice == "4":
            # user["balance"] += 1.0 # delete this, just demonstrating model.save()
            # model.save(user)
            return login_menu()
        if choice == "3":
            amount = round(float(view.enter_deposit_info()), 2)
            model.deposit(user, amount)
            return main_menu(user)
        if choice == "2":
            amount = round(float(view.enter_withdraw_info()), 2)
            answer = model.withdraw(user, amount)
            if answer == 0: 
                view.insufficient_funds()
            return main_menu(user)
        if choice == "1":
            balance = round(model.get_balance(user), 2)
            view.give_balance(balance)


        """ TODO: implement the various options """

     

if __name__ == "__main__":
    run()