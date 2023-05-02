from book import Book


class Member:
    """
    A class representing a library member.

    Attributes:
    -----------
    __member_id : str
        A unique identifier for the member.
    __name : str
        The name of the member.
    __address : str
        The address of the member.
    __phone : str
        The phone number of the member.
    __books_issued : list
        A list of Book objects representing the books issued to the member.

    Methods:
    --------
    __init__(self, member_id: str, name: str, address: str, phone: str)
        Initializes a new instance of the Member class.
    get_member_id(self) -> str
        Returns the member ID of the member.
    get_name(self) -> str
        Returns the name of the member.
    set_name(self, name)
        Sets the name of the member.
    get_address(self) -> str
        Returns the address of the member.
    set_address(self, address)
        Sets the address of the member.
    get_phone(self) -> str
        Returns the phone number of the member.
    set_phone(self, phone)
        Sets the phone of the member.
    get_books_issued(self) -> list[Book]
        Returns a list of Book objects representing the books issued to the member.
    remove_books_issued(self, book) -> None
        Removes input book object from the books issued list of the member.
    issue_book(self, book: Book) -> bool
        Issues a book to the member. Returns True if successful, False otherwise.
    return_book(self, book: Book) -> bool
        Returns a book issued to the member. Returns True if successful, False otherwise.
    """

    def __init__(self, member_id: str, name: str, address: str, phone: str):
        """
        Initializes a new instance of the Member class.

        Parameters:
        -----------
        __member_id : str
            A unique identifier for the member.
        __name : str
            The name of the member.
        __address : str
            The address of the member.
        __phone : str
            The phone number of the member.
        """
        self.__member_id = member_id
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__books_issued = []

    def __str__(self):
        """
        Prints out the title, author, publication year, and ISBN of the book.
        """
        
        return  f"Member Id: {self.__member_id} \n" + \
                f"Name: {self.__name} \n" + \
                f"Address: {self.__address} \n" + \
                f"Phone : {self.__phone} \n" + \
                f"Books Issued: {self.__books_issued} \n" \


    def get_member_id(self) -> str:
        """
        Returns the member ID of the member.
        """
        return self.__member_id

    def get_name(self) -> str:
        """
        Returns the name of the member.
        """
        return self.__name

    def set_name(self, name):
        """
        Sets the name of the member.
        """
        self.__name = name
    
    def get_address(self) -> str:
        """
        Returns the address of the member.
        """
        return self.__address

    def set_address(self, address):
        """
        Sets the address of the member.
        """
        self.__address = address

    def get_phone(self) -> str:
        """
        Returns the phone number of the member.
        """
        return self.__phone
    
    def set_phone(self, phone):
        """
        Sets the phone of the member
        """
        self.__phone = phone

    def get_books_issued(self) -> list[Book]:
        """
        Returns a list of Book objects representing the books issued to the member.
        """
        return self.__books_issued
    
    def remove_book_issued(self, book) -> None:
        """
        Method to edit and remove book from the books issued list for this member
        """
        self.__books_issued.remove(book)

    def issue_book(self, book: Book) -> None:
        """
        Issues a book to the member.

        Parameters:
        -----------
        book : Book
            The Book object to issue to the member.
        """
        self.__books_issued.append(book)

    def return_book(self, book: Book) -> None:
        """
        Returns a book issued to the member.

        Parameters:
        -----------
        book : Book
            The Book object to return.
        """
        self.__books_issued.remove(book)