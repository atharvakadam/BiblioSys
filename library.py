from book import Book
from member import Member
from specialmember import SpecialMember


class Library:
    """
    Represents a library with a collection of books and a list of members.
    
    Attributes:
    -----------
    __library_id (str): The id of the library.
    __name (str): The name of the library.
    __books (List[Book]): A list of books in the library.
    __members (List[Member]): A list of members of the library.
    
    Methods:
    --------
    get_library_id(self) -> str:
        Gets the id of the library

    get_name(self) -> str:
        Gets the name of the library

    get_books(self) -> list[Book]:
        Gets the books of the library

    get_members(self) -> list[Member]:
        Gets the members of the library

    add_book(self, book: Book) -> None:
        Adds a book to the library's collection of books.
        
    remove_book(self, book: Book) -> None:
        Removes a book from the library's collection of books.
        
    add_member(self, member: Member) -> None:
        Adds a member to the library's list of members.
        
    remove_member(self, member: Member) -> None:
        Removes a member from the library's list of members.
        
    lend_book(self, book: Book, member: Member) -> None:
        Lends a book from the library's collection of books to a member.
        
    return_book(self, book: Book, member: Member) -> None:
        Returns a book borrowed by a member to the library's collection of books.
    
    """

    def __init__(self, library_id: str,  name: str):
        """
        Initializes a new instance of the Library class with the given name.
        """
        self.__library_id = library_id
        self.__name = name
        self.__books = []
        self.__members = []
    
    def __str__(self) -> str:
        """
        Overrides the __str__ method of the class to neatly print the Library details
        """
        return  f"Library Name: {self.__name} \n" + \
                f"Number of books: {len(self.__books)} \n" + \
                f"Number of Members: {len(self.__members)} \n"
                
    def get_library_id(self) -> str:
        """
        Gets the id of the library
        """
        return self.__library_id
    
    def get_name(self) -> str:
        """
        Gets the name of the library
        """
        return self.__name

    def set_name(self, name):
        """
        Sets the name of the library
        """
        self.__name = name

    def get_books(self) -> list:
        """
        Gets the books in the library
        """
        return [print(book.get_title()) for book in self.__books]
    
    
    def get_members(self) -> list:
        """
        Gets the Members in the library
        """
        return [print(member.get_name()) for member in self.__members]

    def add_book(self, book: Book) -> None:
        """
        Adds a book to the library's collection of books.

        Parameters:
        -----------
        book (Book): The book to be added to the collection.
        """
        self.__books.append(book)

    def remove_book(self, book: Book) -> None:
        """
        Removes a book from the library's collection of books.

        Parameters:
        -----------
        book (Book): The book to be removed from the collection.
        """
        if book in self.__books:
            self.__books.remove(book)

    def add_member(self, member: Member) -> None:
        """
        Adds a member to the library's list of members.

        Parameters:
        -----------
        member (Member): The member to be added to the list.
        """
        self.__members.append(member)

    def remove_member(self, member: Member) -> None:
        """
        Removes a member from the library's list of members.

        Parameters:
        -----------
        member (Member): The member to be removed from the list.
        """
        if member in self.__members:
            self.__members.remove(member)

    def lend_book(self, book: Book, member: (Member or SpecialMember) ) -> None:
        """
        Lends a book from the library's collection of books to a member.

        Parameters:
        -----------
        book (Book): The book to be lent.
        member (Member): The member to whom the book will be lent.
        """
        try:
            if book in self.__books:
                if book.is_available():
                    if book not in member.get_books_issued():
                        book.lend_copy()
                        member.issue_book(book)
                    else:
                        raise Exception("Member already has one copy of the book! Duplicate copies can't be assigned to same member")
                else:
                    raise Exception("All copies of the book are already lent.")
            else:
                raise Exception("The book is not in the library's collection.")
        except Exception as e:
            print(e)

    def return_book(self, book: Book, member: (Member or SpecialMember)) -> None:
        """
        Returns a book borrowed by a member to the library's collection of books.

        Parameters:
        -----------
        book (Book): The book to be returned.
        member (Member): The member who borrowed the book.
        """
        try:
            if book in member.get_books_issued():
                book.return_copy()
                member.return_book(book)
            else:
                raise Exception("The book was not borrowed by the member.")
        except Exception as e:
            print(e)

