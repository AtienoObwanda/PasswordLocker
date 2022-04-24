import unittest
import pyperclip

from passlock import User
from passlock import Credentials


class TestUser(unittest.TestCase):
    '''
    Test that defines the cases for User class methods

    unittest.TestCase => Test class that helps with the creation of test cases
    '''

    def setUp(self):
        '''
        Initial method that runs before any other methods
        '''
        self.new_user = User("Atieno", "Obwanda", "atienoobwanda@gmail.com","new2022!") #User Object

        def test_init(self):
            '''
            Checks if the object was initialized successfully
            '''
            self.assertEqual(self.new_user.firstName, "Atieno")
            self.assertEqual(self.new_user.lastName, "Obwanda")
            self.assertEqual(self.new_user.email, "atienoobwanda@gmail.com")
            self.assertEqual(self.new_user.password, "atienoobwanda@gmail.com")

        def test_save_user(self):
            '''
            Checks to see if there is a new user created
            '''
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),1)

        def test_delete_user(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_user.save_user()
            test_user = User("Atieno", "Obwanda", "atienoobwanda@gmail.com","new2022!")
            test_user.save_user()

            self.new_user.delete_user()# Deleting user
            self.assertEqual(len(User.user_list),1)            

class TestCredentials(unittest.TestCase):
    '''
    Class that defines test cases for credentials class
    '''
    def setUp(self):

        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential= Credentials("Instagram", "atieno", "xvy123!")

    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.accountName, "Instagram")
        self.assertEqual(self.new_credential.accountUser, "atieno")
        self.assertEqual(self.new_credential.accountPassword, "xvy123!")

    def test_save_account(self):
        """
        test case to test if the credential has been saved into the credentials list.

        """
        self.new_credential.saveAccount()# saving credential
        self.assertEqual(len(Credentials.accounts_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.accounts_list = []

    
    def test_deleteAccount(self):
        '''
        Test delete Account
        '''
        self.new_credential.save_account()
        test_credential = Credentials("Instagram", "atieno", "xvy123!")
        test_credential.save_accounts()

        self.new_credential.deleteAccount()# Deleting credential
        self.assertEqual(len(Credentials.credential_list),1)            




if __name__ == "__main__":
    unittest.main()




