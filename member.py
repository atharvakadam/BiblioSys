from book import Book


class Member:
    """
    A class representing a library member.

    Attributes:
    -----------
    member_id : str
        A unique identifier for the member.
    name : str
        The name of the member.
    address : str
        The address of the member.
    phone : str
        The phone number of the member.
    books_issued : list
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
    get_books_issued(self) -> List[Book]
        Returns a list of Book objects representing the books issued to the member.
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
        member_id : str
            A unique identifier for the member.
        name : str
            The name of the member.
        address : str
            The address of the member.
        phone : str
            The phone number of the member.
        """
        self.member_id = member_id
        self.name = name
        self.address = address
        self.phone = phone
        self.books_issued = []

    def get_member_id(self) -> str:
        """
        Returns the member ID of the member.
        """
        return self.member_id

    def get_name(self) -> str:
        """
        Returns the name of the member.
        """
        return self.name

    def set_name(self, name):
        """
        Sets the name of the member.
        """
        self.name = name
    
    def get_address(self) -> str:
        """
        Returns the address of the member.
        """
        return self.address

    def set_address(self, address):
        """
        Sets the address of the member.
        """
        self.address = address

    def get_phone(self) -> str:
        """
        Returns the phone number of the member.
        """
        return self.phone
    
    def set_phone(self, phone):
        """
        Sets the phone of the member
        """
        self.phone = phone

    def get_books_issued(self) -> List[Book]:
        """
        Returns a list of Book objects representing the books issued to the member.
        """
        return self.books_issued

    def issue_book(self, book: Book) -> bool:
        """
        Issues a book to the member. Returns True if successful, False otherwise.

        Parameters:
        -----------
        book : Book
            The Book object to issue to the member.

        Returns:
        --------
        bool
            True if successful, False otherwise.
        """
        if len(self.books_issued) >= 5:
            return False

        self.books_issued.append(book)
        return True

    def return_book(self, book: Book) -> bool:
        """
        Returns a book issued to the member. Returns True if successful, False otherwise.

        Parameters:
        -----------
        book : Book
            The Book object to return.

        Returns:
        --------
        bool
            True if successful, False otherwise.
        """
        if book not in self.books_issued:
            return False

        self.books_issued.remove(book)
        return True
