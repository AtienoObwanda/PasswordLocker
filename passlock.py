import random
import string
from threading import activeCount
import pyperclip

class User:
    '''
    Class that generates new instances of users

    '''
    userlist=[] #Empty list of users

    def __init__(self, firstName, lastName,  email, password):
        '''
        method that defines the user object
        '''

        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password


    def save_user(self):
        '''
        Method that saves the users
        '''
        User.userlist.append(self)
    @classmethod

    def delete_user(self):
        '''
        Method that deletes the users
        '''
        User.userlist.remove(self)
    @classmethod

    def display_user(cls):
        '''
        Method that displays the user information
        '''
        return cls.userlist
    @classmethod

    def find_email(cls, email):
        '''
        Takes in an email address and returns a list of users that match the email
        '''
        for user in cls.userlist:
            if user.email == email:
                return user
    @classmethod

    def check_user(cls, email):
        '''
        Checks for a user with the given email
        '''
        for user in cls.userlist:
            if user.email == email:
                return True
            else:
                return False



class Credentials:
    '''
    Class for generating credentials
    '''

    accounts=[] #an empty list for accounts

    def __init__(self, accountName, accountUser, accountPassword):
        '''
        Method to define the properties of object self.
        '''
        self.accountName = accountName
        self.accountUser = accountUser
        self.accountPassword = accountPassword
        
    def saveAccount(self):
        '''
        Saves the credentials
        '''
        Credentials.accounts.append(self)

    def deleteAccount(self):
        '''
        Deletes the credentials
        '''
        Credentials.accounts.remove(self)
    @classmethod

    def displayAccount(cls):
        global accounts
        '''
        Returns active accounts
        '''
        for account in cls.accounts:
            return cls.accounts 
    @classmethod

    def findAccount(cls, accountName):
        '''
        A method that takes in the email address and returns the account associated with that email
        '''
        for account in cls.accounts:
            if accounts.accountName == accountName:
                return account
            else:
                print("Oops... account not found!")







    
    

        

