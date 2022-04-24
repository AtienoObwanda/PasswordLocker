import random
import string
import pyperclip

class User:
    '''
    Class that generates new instances of users
    '''
    userlist=[]

    def __init__(self, firstName, lastName,  email, password):
        '''
        method that defines the user object
        '''

        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        
        
