import unnitest

from passlock import User

class TestUser(unittest.TestCase):
    '''
    Test that defines the cases for User class methods
    '''

    def setUp(self):
        '''
        Initial method that runs before any other methods
        '''
        self.new_user = User("Atieno Obwanda")