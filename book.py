class Book:
    """
    A class to represent a book.

    Attributes
    ----------
    title : str -> The title of the book.
    author : str -> The author of the book.
    publication_year : int -> The year the book was published.
    ISBN : str -> The International Standard Book Number for the book.
    num_copies : int -> The number of copies of the book that the library owns.
    num_copies_available : int -> The number of copies of the book that are currently available to be borrowed.

    Methods
    -------
    display_info() -> Prints out the title, author, publication year, and ISBN of the book.
    increase_copies(num) -> Increases the number of copies of the book that the library owns by the specified number.
    decrease_copies(num) -> Decreases the number of copies of the book that the library owns by the specified number.
    is_available() -> Returns True if there are any available copies of the book, False otherwise.
    """


    def __init__(self, title, author, publication_year, ISBN, num_copies, fiction_genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN = ISBN
        self.num_copies = num_copies
        self.num_copies_available = num_copies
        self.fiction_genre = fiction_genre

    def display_info(self):
        """
        Prints out the title, author, publication year, and ISBN of the book.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"ISBN: {self.ISBN}")

    def get_title(self):
        """
        Gets the title of the book.
        """
        return self.title

    def get_author(self):
        """
        Gets the author of the book.
        """
        return self.author

    def get_publication_year(self):
        """
        Gets the publication year of the book.
        """
        return self.publication_year

    def get_ISBN(self):
        """
        Gets the ISBN of the book.
        """
        return self.ISBN

    def get_num_copies_available(self):
        """
        Gets the number of copies of the book.
        """
        return self.get_num_copies_available
    
    def get_fiction_genre(self):
        """
        Gets the genre of the book -> either fiction or non-fiction
        """
        return self.get_fiction_genre
    
    def set_fiction_genre(self, fiction_genre):
        """
        Sets the genre of the book to either fiction or non-fiction
        """
        self.fiction_genre = fiction_genre

    def increase_copies(self, num):
        """
        Increases the number of copies of the book that the library owns by the specified number.

        Parameters
        ----------
        num : int
            The number of copies to add.
        """
        self.num_copies += num
        self.num_copies_available += num

    
    def decrease_copies(self, num):
        """
        Decreases the number of copies of the book that the library owns by the specified number.

        Parameters
        ----------
        num : int
            The number of copies to remove.
        """
        if num > self.num_copies_available:
            raise ValueError("Cannot remove more copies than are available.")
        self.num_copies -= num
        self.num_copies_available -= num

    def is_available(self):
        """
        Returns True if there are any available copies of the book, False otherwise.
        """
        return self.num_copies_available > 0