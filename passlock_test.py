import unittest
import pyperclip

from passlock import User


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

class TestCredentials(unittest.TestCase):
    




if __name__ == "__main__":
    unittest.main()




