#!
from user import User, Credentials


def create_new_user(username,password):
   
    new_user = User(username,password)
    return new_user

def save_user(user):
  
    user.save_user()
def display_user():
   
    return User.display_user()
def login_user(username,password):
   
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_accounts(credentials):
   
    credentials. save_details()
def display_accounts_details():
    
    return Credentials.display_accounts()

def delete_credential(credentials):
 
    credentials.delete_accounts()

def find_credential(account):
   
    return Credentials.find_credential(account)
def check_credendtials(account):
    
    return Credentials.if_credential_exist(account)

def generate_Password():
    
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
  
    return Credentials.copy_password(account)


def passlocker():
    print("----------------------------------------------------------------")
    print("|                WELCOME TO PASSWORD BANK                      |")
    print("----------------------------------------------------------------")
    print('\n')
    print("Don't Know about you, but I've personally ran out of password memory...")
    print('\n')
      
    print("**That's where Pass Bank comes in!**")
    print('\n')
    print('\n')
    print("1. Sign Up for new account ---> SU    \n2. Sign In  tp your account ---> SI \n")
    choice=input("").lower().strip()
    if choice == "su":
        print("Sign Up")
        print("----------------------------------------------------------------")
        username = input("Preferred username: ")
        while True:
            print("Reply with: \nE -> Enter your own pasword: \nG -> To generate a Password: ")
            password_Choice = input().lower().strip()
            if password_Choice == 'e':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'g':
                password = generate_Password()
                break
            else:
                print("Invalid password")
        save_user(create_new_user(username,password))
        print("-----------------------------------------------------------------------------")
        print(f"Dear, {username}! Congratulations, account has been created successfully!")
        print("------------------------------------------------------------------------------")
        
    elif choice == "si":
        print("----------------------------------------------------------------")
        print("Enter your details to log in:")
        print("----------------------------------------------------------------")

        username = input("Enter your: ")
        password = input("Enter yourpassword: ")
        login = login_user(username,password)
        if login_user == login:
            print("----------------------------------------------------------------")
            print(" Sign In successful!")  
            print("----------------------------------------------------------------")

            print('\n')
    while True:
        print("To get started, reply with:\nCreate a new credential --> CC \nView Credentials --> VC  \nSearch Credential --> SC \nGenerate password --> G \nDelete --> D \nExit the application -->  E \n")
        choice = input().lower().strip()
        if choice == "cc":
            print("Add Credential")
            print("----------------------------------------------------------------")
            print("Account name: ")
            account = input().lower()
            print("Account username: ")
            userName = input()
            while True:
                print("Reply with: \nT - To enter your own pasword:\nG - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 't':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'g':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_accounts(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created successfully")
            print('\n')
        elif choice == "vc":
            if display_accounts_details():
                print("Here's your list of accounts: ")
                 
                print("----------------------------------------------------------------")
                for account in display_accounts_details():
                    print(f" Account:{account.account} \nUser Name:{username}\nPassword:{password}")
                    print("----------------------------------------------------------------")
            else:
                print("You don't have any credentials saved yet..........")
        elif choice == "sc":
            print("Enter the Account Name: ")
            print("----------------------------------------------------------------")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print("----------------------------------------------------------------")
                print(f"Username: {search_credential.userName} Password :{search_credential.password}")
                print("----------------------------------------------------------------")
            else:
                print("Credential couldn't be found")
                print('\n')
        elif choice == "d":
            print("Enter the account name to proceed")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("----------------------------------------------------------------")
                search_credential.delete_accounts()
                print('\n')
                print(f" {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("Failed: Credential not found")

        elif choice == 'g':

            password = generate_Password()
            print(f"Generated Password: {password}")
        elif choice == 'ex':
            print("Exiting password bank...")
            break
        else:
            print("Invalid entry")
    else:
        print("Enter a valid input")

if __name__ == '__main__':
    passlocker()