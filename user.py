import random
import string
import pyperclip
class User:
    """
    Create User class that generates new instances users.

    """
    users = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.users.append(self)
    

    @classmethod
    def display_user(cls):
        return cls.users

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.users.remove(self)

class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    accounts = []
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our users or not
        """
        a_user = ""
        for user in User.users:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.accounts.append(self)

    def delete_accounts(self):
        """
        delete_accounts method that deletes an account credentials from the accounts
        """
        Credentials.accounts.remove(self)
    
    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.

        """
        for credential in cls.accounts:
            if credential.account == account:
                return credential
    @classmethod
    def copy_password(cls,account):
        found_accounts = Credentials.find_credential(account)
        pyperclip.copy(found_accounts.password)

    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.accounts:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_accounts(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.accounts

    def generatePassword(stringLength=10):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))