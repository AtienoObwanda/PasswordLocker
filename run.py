#! 
import string
import random
from passlock import User
from passlock import Credentials

def createUser(fName, Lname, uName, email, pWord):
    newUser = User(fName, Lname, uName, email, pWord)
    return newUser

def saveUser(user):
    user.save_user()

def deleteUser(user):
    user.delete_user()

def displayUser(email):
    return User.findByEmail(email)

def createAccount(accountName, accountUser, accountPassword):
    newaccount=(accountUser, accountName, accountPassword)
    return newaccount

def save_account(user):
    user.saveAccount()

def delete_account(user):
    user.deleteAccount()

def findAccount(email):
    return Credentials.findAccount(email)

def display_account():
    return Credentials.displayAccount()


def main():
   
        print("----------------------------------------------------------------")
        print("|                WELCOME TO PASSWORD BANK                      |")
        print("----------------------------------------------------------------")
        print('\n')
        print("Don't Know about you, but I've personally ran out of password memory...")
        print('\n')
      
        print("****That's where Pass Bank comes in!****")
        print('\n')
        print('\n')
    
        
        
        username = input("What is your name? ")
        print("----------------------------------------------------------------")


        print("Hello " + username +" " + "what would you like to do?")
        print('\n')
        print('\n')

while True:
    print("----------------------------------------------------------------")
    print("To proceed, kindly enter the code that applies: ")
    print('\n')

    print("Sign Up ----> SU")
    print('\n')

    print("Login----->LG")
    print('\n')

    inp=input("Make a choice... ")

    print("----------------------------------------------------------------")
    print('\n')
    
    if inp=="SU":
        print("SIGN UP FOR PASS BANK")
        print("----------------------------------------------------------------")
        fName=input("Enter your first name: ")
        lName=input("Enter your last name: ")
        uName=input("Enter your username: ")
        # if lName.len > 4:
        #     print("User name must be at least 4 characters...")
        # else:
        email=input("Enter your email address: ")
        pWord=input("Enter your password: ")
            # if pWord==1234:
            #     print ("Please enter a strong password")

        saveUser(creteUser(fName, lName, uName, email, pWord))
        print("----------------------------------------------------------------")
        print("Congratulations, account has been created successfully!")
        print("----------------------------------------------------------------")
        print(r"Name: {fName} {lName} \Username: {uName} \nEmail: {email} \password: {pWord}")
        print('\n')
        print("----------------------------------------------------------------")
        inp=input("Enter LG to proceed to Login-----> LG")
        print("----------------------------------------------------------------")
    elif inp=="LG":
        loginEmail=input("Enter your email: ")
        print('\n')
        loginPassword=input("Enter your password: ")
        print("----------------------------------------------------------------")
        if displayUser(loginEmail, loginPassword):
            print("\n")
            choice=input("You can: 1. Create new pass bank-->AC \n2. View existing passwords-->VC \n: ")
            print('\n')
            print("----------------------------------------------------------------")

            if choice == "AC":
                print("-----------------------------------------------------")
                print("                ADD NEW PASSWORD                     ")
                print("-----------------------------------------------------")

                accountEmail=loginEmail
                accountName=input("Enter the name of the account: ")
                print('\n')
                accountUser=input("Enter the account username: ")
                print('\n')
                generatePassword=input("Would you like to generate a password? reply with Y/N: ")
                if generatePassword == "Y":
                    characters=string.ascii.letters + string.digits
                    accountPassword="".join(choice(characters) for x in range(random.randint(8,18)))
                    print(f"Generated password: {accountPassword}")
                elif generatePassword == "N":
                   accountPassword= input("Enter your password: ")
                else:
                    print("Please input a valid password!")

                save_account(createAccount(accountUser, accountName,accountEmail, accountPassword))
                
                print("----------------------------------------------------------------")
                print('\n')
                print(f"Account Name:{accountName} \nAccount Email: {accountEmail}\n Username: {accountUser} \n Password: {accountPassword}")
                print('\n')
                print("----------------------------------------------------------------")

            elif choice =="VC":
                findAccount(accountEmail)
                print("Active accounts:")
                print("----------------------------------------------------------------")
                for user in display_account():
                    print(r"Account: {user.accountName} \n Email: {user.accountEmail}\n Username: {user.accountUser} \n Password: {user.accountPassword}")
            
                else:
                    print("Invalid credentials!!!")
        
            else:
                print("Invalid choice, please try again:")
                print('\n')
        else:
            print("Incorrect info, please try again")
            print('\n')
    else:
        print("Kindly choose a valid Option")
        print('\n')

if __name__ == '__main__':
    main()










