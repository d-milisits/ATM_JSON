#controller imports model and view and calls all the functions 
#model is the logic 
#view is the print statements/user interface stuff
def PIN_prompt():
    return input("Please enter your 4 digit PIN number now: ")

def acc_num_prompt():
    return input("Please enter your account number.")

def pin_error():
    print("\nPin not found in database. Try again")
    # PIN_prompt()

def main_menu():
    print("Please select one of the following options:\n")
    print("1). Create new Account")
    print("2). Log in")
    print("3). Exit")

def new_account_success():
    print("\nYou have created a new account.\n\n")

def create_pin():
    return input("\nPlease type your new PIN below. \n")

def option_prompt():
    return input("Select one of the above options now. ")

def user_options():
    print("\nWould you like to:\n1). Withdraw?\n2). Deposit?\n3). Check current balance?\n")

def specify_amount():
    return input("Please specify the amount: \n")

def exit():
    print("Exiting...\n")
