import unittest
from book import Book
from library import Library
from member import Member
'''
This file imports the unittest module which is used to write unit tests in python. We are using this to currently test
basic object creations/initializations of Book, Library and Member classes.

More unit test cases can be added to make the test suite more robust.
'''


class TestMember(unittest.TestCase):
    '''
    This class is for testing all member functionality.
    '''
   
    def test_create_member1(self):
        '''
        Test designed to pass, member creation should be successful
        '''
        member = Member("1s23", "John Doe", "3533 Lark Ave", "352-353-2233")
        assert isinstance(member,Member)
        print('Member creation test 1 - Passed successfully')

   
    def test_create_member2(self):
        '''
        Test designed to pass, member creation should be successful
        '''
        member = Member("1s23", "John Doe", "3533 Lark Ave", "352-353-2233")
        assert isinstance(member,Member)
        print('Member creation test 2 - Passed successfully')

class TestLibrary(unittest.TestCase):
    '''
    This class is for testing all library functionality.
    '''
    
    def test_create_library1(self):
        '''
        Test designed to fail, library creation should be fail because of incorrect number of parameters passed in
        '''
        libr = Library("1s23", 'Queens County', '12')
        assert isinstance(libr,Library)
        print('Library creation test 1 - Passed successfully')

    
    def test_create_library2(self):
        '''
        Test designed to pass, book creation should be successful
        '''
        libr = Library("1s23", 'Queens County')
        assert isinstance(libr,Library)
        print('Library creation test 2 - Passed successfully')

class TestBook(unittest.TestCase):
    '''
    This class is for testing all book functionality.
    '''
    
    def test_create_book1(self):
        '''
        Test designed to fail, since incorrect number of parameters passed in while object creation
        '''
        book = Book("Astrophysics for people in a hurry", "Neil Degrasse Tyson", 2017, '224-25255-22', 3)
        assert isinstance(book,Book)
        print('Book creation test 1 - Passed successfully')

    
    def test_create_book2(self):
        '''
        Test designed to pass, book creation should be successful
        '''
        book = Book("Astrophysics for people in a hurry", "Neil Degrasse Tyson", 2017, '224-25255-22', 3, False)
        assert isinstance(book,Book)
        print('Book creation test 2 - Passed successfully')

if __name__ == '__main__':
    unittest.main()

