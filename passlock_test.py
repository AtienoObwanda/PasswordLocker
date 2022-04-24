import unnitest

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