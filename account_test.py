import unittest
import pyperclip
from account import User
from account import Account
 

class testUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''      
        Set up method to run before each test cases.
        '''
        self.new_user = User("mwalo","mwalo9214") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.lockname,"mwalo")
        self.assertEqual(self.new_user.password,"mwalo9214")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user's object is saved into the user's list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):

	    '''
		delete user's account
		'''

	    self.new_user.save_user()

	    test_user=User("mwalo254","mwalo254")
	    test_user.save_user()
	    self.new_user.delete_user()
	    self.assertEqual(len(User.user_list),1)

class testAccounts(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def test_check_user(self):
    
        '''
		Function to test whether the login in function check_user works as expected
		'''
        self.new_user = User("mwalo254","mwalo254")
        self.new_user.save_user()
        user2 = User('nick','nick9214')
        user2.save_user()

        for user in User.user_list:
            if user.lockname == user2.lockname and user.password == user2.password:
	            current_user = user.lockname
        return current_user

        self.assertEqual(current_user,Account.check_user(user2.password,user2.lockname))


    def setUp(self):
        '''      
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Github","mwalo254","mwalo9214")



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.somedia,"Github")
        self.assertEqual(self.new_account.username,"mwalo254")
        self.assertEqual(self.new_account.accpassword,"mwalo9214")

    # def test_save_account(self):
    #     '''
    #     test_save_account test case to test if the account object is saved into
    #      the account list
    #     '''
    #     self.new_account.save_account()
    #     self.assertEqual(len(Account.account_list),1)

    def test_save_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            codewars= Account("Codewars","mwalo254","user11") 
            codewars.save_account()
            self.assertEqual(len(Account.account_list),2)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []
            User.user_list=[]

    def test_display_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''
        self.new_account.save_account()
        codewars = Account('Codewars', 'mwalz','user')
        codewars.save_account()
        gmail= Account('Gmail','mwalznick','mwalz9214')
        gmail.save_account()
        self.assertEqual(len(Account.display_accounts(codewars.somedia)),3)

    def test_find_by_somedia(self):
        '''
		Test to check if the find_by_somedia method returns the correct account
		'''
        self.new_account.save_account()
        codewars = Account('Codewars','mwalz','user')
        codewars.save_account()
        account_exists = Account.find_by_somedia('Codewars')
        self.assertEqual(account_exists,codewars)



    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Codewars","mwalz","user")
            test_account.save_account()

            self.new_account.delete_account()
            self.assertEqual(len(Account.account_list),1)


    def test_copy_account(self):
        '''
		test to check if the copy an account method copies the correct account
		'''
        self.new_account.save_account()
        codewars= Account('Codewars','mwalz','user')
        codewars.save_account()
        find_account = None

        for account in Account.user_account_list:
            find_account=Account.find_by_somedia(account.somedia)
            return pyperclip.copy(find_account.accpassword)

        Account.copy_account(self.new_account.somedia)
        self.assertEqual('mwalo9214',pyperclip.paste())
        print(pyperclip.paste())

    

    



if __name__ == '__main__':
    unittest.main()