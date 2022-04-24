import random
import string
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

    def findByEmail(cls, email):
        '''
        Takes in an email address and returns a list of users that match the email
        '''












    
    

        

