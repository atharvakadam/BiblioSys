class Book:
    # fiction/nonfiction - only two genres for simplicity
    def __init__(self, title, author, publication_date, book_id, fiction_genre):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.book_id = book_id
        self.is_available = True
        self.fiction_genre = fiction_genre

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publication_date(self):
        return self.publication_date

    def get_book_id(self):
        return self.book_id

    def get_is_available(self):
        return self.is_available
    
    def get_fiction_genre(self):
        return self.get_fiction_genre

    def set_is_available(self, is_available):
        self.is_available = is_available
    
    def set_fiction_genre(self, fiction_genre):
        self.fiction_genre = fiction_genre


