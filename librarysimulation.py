from datetime import datetime, timedelta
from random import randint
import random

# Import classes from previous implementation
from book import Book
from member import Member
from library import Library
from specialmember import SpecialMember

class LibrarySimulation:
    def __init__(self):
        # Create an instance of the library
        self.library = Library('1a', 'Queens County')

        # Create some books and add them to the library
        self.books = [
            Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, '123-22-333-4565', 5, True),
            Book("The Catcher in the Rye", "J.D. Salinger", 1951, '535-332-333-4565', 2, True),
            Book("To Kill a Mockingbird", "Harper Lee", 1960, '775-332-333-4565', 3, True),
            Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, '885-332-333-4565', 5, True)
        ]
        for book in self.books:
            self.library.add_book(book)

        # Create some members and add them to the library
        self.members = [
            Member("1afs35","Alice", "5038 W Lark Ave", "333-725-3335"),
            Member("2afs35","Alex", "1234 W Park Ave", "923-725-3335"),
            Member("3afs35","Robert", "5353 W Lincon Street", "536-725-3335"),
            SpecialMember("4asf34","Bob", "2453 W Downy Street", "646-725-3335"),
            SpecialMember("dgdf34","Gary", "3553 W Regan Street", "646-725-3335")
        ]
        for member in self.members:
            self.library.add_member(member)

    # Add test cases here that can be called in the run function. Run function can go through all test cases one by one.
    def test1(self):
        pass   

    def run(self):
        # Check all the books that library currently has
        print("======Books currently owned by the library======")
        self.library.get_books()
        print("================================================")
        print()

        # Check all the members that library currently has
        print("========All current library members=============")
        self.library.get_members()
        print("================================================")
        print()

        # Testing if removing book from the library works.
        print("===========Removing book from library===========")
        print("Library before removing 'To Kill a Mockingbird' ")
        print(self.library)
        self.library.remove_book(self.books[2])
        print("Library after removing 'To Kill a Mockingbird': ")
        print(self.library)

        print("Trying to lend the removed book:")
        # this should throw an error
        self.library.lend_book(self.books[2],self.members[0])
        print("================================================")
        print()

        # Testing if removing member from the library works.
        print("========Removing Member from library============")
        print("Library before removing member Alice ")
        print(self.library)
        self.library.remove_member(self.members[0])
        print("Library after removing member Alice ")
        print(self.library)

        print("Trying to lend a book to a non member:")
        # this should throw an error
        self.library.lend_book(self.books[1],self.members[0])
        print("================================================")
        print()

        # Testing successful lending of book to a member
        print("======Lending and returning book to member======")

        print("Trying to lend a book to a member:")
        print("Number of available copies for book before -> ", self.books[1].get_num_copies_available())
        self.library.lend_book(self.books[1],self.members[1])
        print("Number of available copies for book after -> ", self.books[1].get_num_copies_available())
        

        print("Trying to return a book from member to library:")
        self.library.return_book(self.books[1],self.members[1])
        print("Number of available copies for book after -> ", self.books[1].get_num_copies_available())
        print("================================================")
        print()

        # Testing successful lending of book to a special member
        print("==Lending and returning book to special member==")

        print("Trying to lend a book to a special member:")
        print("Number of available copies for book before -> ", self.books[1].get_num_copies_available())
        self.library.lend_book(self.books[1],self.members[3])
        print("Number of available copies for book after -> ", self.books[1].get_num_copies_available())
        

        print("Trying to return a book from member to library:")
        self.library.return_book(self.books[1],self.members[3])
        print("Number of available copies for book after -> ", self.books[1].get_num_copies_available())

        print()
        # special member should have 10 reward points for having read a book
        print("The special member has 10 reward points: ")
        print(self.members[3])
        print("=================================================")
        print()

        # Testing successful claim of reward by a special member
        print("=====Special member trying to redeem reward======")

        # special member should have 10 reward points for having read a book
        print("The special member has 10 reward points: ")
        print(self.members[3])

        print("The special member is trying to claim a subscription reward")
        self.members[3].redeem_reward('subscription')
        print(self.members[3])

        # this should throw an error message displaying not enough points
        print("The special member is trying to claim a discount reward")
        self.members[3].redeem_reward('discount')
        print()


        print("=================================================")
        print()





if __name__ == '__main__':
    sim1 = LibrarySimulation()
    sim1.run()