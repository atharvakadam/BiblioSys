class Book:
    """
    A class to represent a book.

    Attributes
    ----------
    __title : str -> The title of the book.
    __author : str -> The author of the book.
    __publication_year : int -> The year the book was published.
    __ISBN : str -> The International Standard Book Number for the book.
    __num_copies : int -> The number of copies of the book that the library owns.
    __num_copies_available : int -> The number of copies of the book that are currently available to be borrowed.
    __fiction_genre: bool -> For the sake of simplicity the genre of the book will be either fiction or nonfiction hence bool value.
    
    Methods
    -------
    display_info() -> Prints out the title, author, publication year, and ISBN of the book.
    get_title() ->  Gets the title of the book
    Set_title() ->  Sets the title of the book
    get_author() -> Gets the author of the book
    set_author() -> Sets the author of the book
    get_publication_year() -> Gets the publication year of the book
    set_publication_year() -> Sets the publication year of the book
    get_ISBN -> Gets the ISBN of the book.
    set_ISBN -> Sets the ISBN of the book.
    get_num_copies_available -> Get numbe rof copies that are currently available to the borrow
    get_fiction_genre -> Get the fiction genre of the book
    set_fiction_genre(fiction_genre) -> Sets the fiction genre bool value for that book
    increase_copies(num) -> Increases the number of copies of the book that the library owns by the specified number.
    decrease_copies(num) -> Decreases the number of copies of the book that the library owns by the specified number.
    is_available() -> Returns True if there are any available copies of the book, False otherwise.
    """

    def __init__(self, title: str, author: str, publication_year: int, ISBN: str, num_copies: int, fiction_genre: bool):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__ISBN = ISBN
        self.__num_copies = num_copies
        self.__num_copies_available = num_copies
        self.__fiction_genre = fiction_genre

    def __str__(self) -> str:
        """
        Overriding the string method of the class to print the title, author, publication year, and ISBN of the book.
        """ 
        
        return  f"Title: {self.__title} \n" + \
                f"Author: {self.__author} \n" + \
                f"Publication Year: {self.__publication_year} \n" + \
                f"ISBN: {self.__ISBN} \n" + \
                f"Number of copies owned: {self.__num_copies} \n" + \
                f"Number of copies available: {self.__num_copies_available} \n" + \
                f"Genre: {'Fiction' if self.__fiction_genre else 'Non-Fiction'} \n"

    def get_title(self) -> str:
        """
        Gets the title of the book.
        """
        return self.__title
    
    def set_title(self, title):
        """
        Sets the title of the book.
        """
        self.__title = title

    def get_author(self) -> str:
        """
        Gets the author of the book.
        """
        return self.__author

    def set_author(self, author):
        """
        Sets the author of the book.
        """
        self.__author = author
    
    def get_publication_year(self) -> int:
        """
        Gets the publication year of the book.
        """
        return self.__publication_year

    def set_publication_year(self, publication_year):
        """
        Sets the publication year of the book.
        """
        self.__publication_year = publication_year

    def get_ISBN(self) -> str:
        """
        Gets the ISBN of the book.
        """
        return self.__ISBN

    def set_ISBN(self, ISBN):
        """
        Sets the ISBN of the book.
        """
        self.__ISBN = ISBN

    def get_num_copies(self) -> int:
        """
        Gets the number of copies of the book owned by the library
        """
        return self.__num_copies
    
    def get_num_copies_available(self) -> int:
        """
        Gets the number of copies of the book.
        """
        return self.__num_copies_available
    
    def get_fiction_genre(self) -> bool:
        """
        Gets the genre of the book -> either fiction or non-fiction
        """
        return self.__fiction_genre
    
    def set_fiction_genre(self, fiction_genre):
        """
        Sets the genre of the book to either fiction or non-fiction
        """
        self.__fiction_genre = fiction_genre

    def increase_copies(self, num):
        """
        Increases the number of copies of the book that the library owns by the specified number.

        Parameters
        ----------
        num : int
            The number of copies to add.
        """
        self.__num_copies += num
        self.__num_copies_available += num

    
    def decrease_copies(self, num):
        """
        Decreases the number of copies of the book that the library owns by the specified number.

        Parameters
        ----------
        num : int
            The number of copies to remove.
        """
        if num > self.__num_copies_available:
            raise ValueError("Cannot remove more copies than are available.")
        self.__num_copies -= num
        self.__num_copies_available -= num

    def is_available(self) -> bool:
        """
        Returns True if there are any available copies of the book, False otherwise.
        """
        return self.__num_copies_available > 0