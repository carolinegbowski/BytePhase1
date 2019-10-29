import view
import class_model as m

model = m.Model()

def run(): 
    while True:
        user_account = login_menu()  # returns the logged in user or None for quit
        if user_account == None:  # login menu returns None if 'quit' is selected
            break
        else:
            main_menu(user_account)  # when the user exits the main menu they will go back to login

def login_menu():
    """ Login Menu - Create Account / Log In / Quit """
    while True:
        view.print_login_menu()
        choice = view.login_menu_prompt().strip()
        if choice not in ("1", "2", "3"):
            """ bad input """
            view.bad_login_input()
            return login_menu()
        elif choice == "3":
            """ 3. Quit """
            view.goodbye()
            return None # return None for quit

        elif choice == "1":
            """ 1. Create Account """
            create_account()

        elif choice == "2":
            """ 2. Log In """
            account = view.login_account_num()
            pin = view.login_pin()
            account_data = model.login(account, pin)
            if account_data != None: 
                return main_menu(account_data)
            else: 
                view.bad_account_login()

def create_account():
    """ 2. Create Account -- called from main menu"""
    view.new_account_creation()
    first_name = view.first_name()
    last_name = view.last_name()
    pin = view.pin()
    confirmed_pin = view.confirm_pin()
    initial_balance = view.initial_balance()
    """ checking if acct / pin are correct"""
    if pin == confirmed_pin:
        new_user = m.Model(first=first_name, last=last_name, balance=initial_balance, pin=pin)
        new_account_number = new_user.save()
        view.new_account_number(new_account_number) 
    else: 
        view.pin_not_confirmed()
        return

def main_menu(user):
    """ Main Menu - Check Balance/ Deposit / Withdraw / Quit """
    while True:
        view.print_main_menu(user)
        choice = view.main_prompt()
        if choice not in ("1", "2", "3", "4"):
            """ Bad Input """ 
            view.bad_login_input()
            return main_menu(user)
        elif choice == "4":
            """ 4. Log Out """
            # user["balance"] += 1.0 # delete this, just demonstrating model.save()
            # model.save(user)
            return login_menu()
        elif choice == "3":
            """ 3. Deposit """
            amount = round(float(view.enter_deposit_info()), 2)
            model.deposit(user, amount)
            return main_menu(user)
        elif choice == "2":
            """ 2. Withdraw """
            amount = round(float(view.enter_withdraw_info()), 2)
            answer = model.withdraw(user, amount)
            if answer == 0: 
                view.insufficient_funds()
            return main_menu(user)
        elif choice == "1":
            """ 1. Check Balance """
            balance = round(model.get_balance(user), 2)
            view.give_balance(balance)
     
if __name__ == "__main__":
    run()

