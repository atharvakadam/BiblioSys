from library import Library
from book import Book
from member import Member

class Simulation:
    def main():
        libr = Library('123', 'Athenaeum')
        print(libr)
        book1 = Book('asdfas','Atharvq', 2222, '241', 2, True)
        book2 = Book('dsafs','Athardsavq', 2222, '2b41', 2, False)
        book3 = Book('httr','Atharddddddvq', 2222, '2d41', 2, True)

        libr.add_book(book1)
        libr.add_book(book2)
        libr.add_book(book3)

        libr.get_books()
        print()

        libr.remove_book(book2)

        libr.get_books()
        print()

        print(libr)
        print()

        member1 = Member('123', 'Atharva', 'asdf 223 212', '123431222')
        member2 = Member('233', 'Avik', 'fsdaf 223 212', '652373533')
        member3 = Member('443', 'Gaurav', 'gdgd 223 212', '351253253')

        libr.add_member(member1)
        libr.add_member(member2)
        libr.add_member(member3)


        print(libr)
        libr.get_members()

        print()
        libr.remove_member(member2)

        libr.get_members()
        print(libr)
        # print(libr.get_books())
        # print()
        # print(libr)

        print(book1.get_num_copies())
        print(book1.get_num_copies_available())
        print(member1.get_books_issued())
        libr.lend_book(book1, member1)
        print(book1.get_num_copies())
        print(book1.get_num_copies_available())
        print(member1.get_books_issued())

        print()
        libr.return_book(book1, member1)
        print(book1.get_num_copies_available())
        print(member1.get_books_issued())

    if __name__ == "__main__":
        main()