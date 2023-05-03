# BiblioSys

This is a Python implementation of a library management system that allows for the management of books and members, as well as lending and returning of books.

## Table of Contents

-  Installation
-  Usage
-  Classes
-  Testing
-  Contributing
-  License

## Installation

To run this program, you must have Python 3 installed. Clone the repository and navigate to the root directory.
```
git clone https://github.com/example/library-management-system.git
cd library-management-system
```

## Usage

To use the Library Management System, import the necessary classes from the library package. Here is an example of how to create a library, add books, and add members:

```
from book import Book
from member import Member
from library import Library

# Create a library
library = Library('1a','Main Library')

# Add books to the library

book1 = Book('Book 1', 'Author 1', 1999, '2342-222-222-432', 3, False)
book2 = Book('Book 2', 'Author 2', 1999, '5555-222-222-432', 5, False)
library.add_book(book1)
library.add_book(book2)

# Add members to the library
member1 = Member('001', 'John Doe', '3533 Lark Ave', '555-1234')
member2 = Member('002', 'Jane Doe', '2234 Park Ave', '555-5678')
library.add_member(member1)
library.add_member(member2)
```

You can also lend books to members and return them:

```
# Lend a book to a member
library.lend_book(book1, member1)

# Return a book from a member
library.return_book(book1, member1)
```

Special members can accumulate reward points and redeem them for rewards:

```
from library import SpecialMember, Rewards

# Create a special member
special_member = SpecialMember('001', 'John Doe', '2234 Moorpark Ave', '555-1234')

# Lend a book to a special member
library.lend_book(book1, special_member)

# Return a book from a special member
library.return_book(book1, special_member)

# Check reward points and redeem rewards
print(special_member.get_reward_points())  # Output: 10
# Special member can redeem any of the three reward types available -> discount, subscription or cashback
special_member.redeem_reward('subscription')
```

## Classes

The library management system consists of the following classes:

### Book

This class represents a book in the library. It has the following attributes:

-   `title` (string): the title of the book
-   `author` (string): the author of the book
-  	 `publication_year (int)`: the publication year of the book
-   `ISBN` (string): the ISBN of the book
-   `num_copies` (int): the total number of copies of the book owned by the library
-   `num_available_copies` (int): the number of copies of the book that are currently available in the library
-   `fiction_genre` (bool): the genre of the book is fiction or non-fiction (only two genres available for simplicity)

And the following methods:

-   `get_num_copies_available`: gets number of avalilable copies of the book in the library
-   `lend_copy`: decrements the number of copies available for the book by 1 as it lends a copy to the member
-   `return_copy`: increments the number of copies available by  1 as it receives a returned copy from the member
-   `increase_copies`: adds copies of a book to the library so number of copies owned goes up
-   `decrease_copies`: removes copies from from the library so number of copies owned goes down
-   `is_available`: checks if number of available copies for the book is > 0


### Member

This class represents a member of the library. It has the following attributes:

-   `member_id` (int): the unique ID of the member
-   `name` (string): the name of the member
-   `address` (string): the address of the member
-   `phone` (string): the phone of the member
-   `books_issued` (list): a list of books that the member has currently borrowed from the library

And the following methods:

-   `get_books_issued`: gets all the books issued from the library
-   `issue_book`: issues a new book from the library
-   `return_book`: returns a book to the library

### Library

This class represents the library itself. It has the following attributes:

-   `library_id` (list): the id of the library
-   `name` (list): name of the library
-   `books` (list): a list of all books in the library
-   `members` (list): a list of all members of the library

And the following methods:

-   `get_books`: gets all books in the library
-   `get_members`: gets all members of the library
-   `add_book`: adds a new book to the library
-   `remove_book`: removes a book from the library
-   `add_member`: adds a new member to the library
-   `remove_member`: removes a member from the library
-   `lend_book`: lends a book to a member
-   `return_book`: returns a book to the library

### SpecialMember

This class represents a special member of the library who can earn reward points. It inherits from the Member class and has the following additional attributes:

-   `reward_points` (int): the number of reward points that the special member has accumulated
-   `reward_benchmark` (int): the number of reward points that are required to claim a reward

And the following methods:

-   `return_book`: returns a borrowed book back to the library
-   `redeem_reward`: redeems a reward based on choice of reward type and adds it to the reward list

### Rewards

This is an Abstract base class which represents the rewards that can be earned by a special member. It is intended as an interface and it has the following method:

-   `issue_reward`: issues a randomized reward coupon that is added to the rewards of the special member

### SubscriptionRewards

This is an implementation of the Rewards class which represents the subscription based rewards that can be earned by a special member. 

Includes the implementation of the `issue_reward` function defined in the Rewards interface:

-   `issue_reward`: For this instance issues a randomized subscription based reward coupon that is added to the rewards of the special member

### DiscountRewards

This is an implementation of the Rewards class which represents the discount based rewards that can be earned by a special member. 

Includes the implementation of the `issue_reward` function defined in the Rewards interface:

-   `issue_reward`: For this instance issues a randomized discount based reward coupon that is added to the rewards of the special member

### CashbackRewards

This is an implementation of the Rewards class which represents the cashback based rewards that can be earned by a special member. 

Includes the implementation of the `issue_reward` function defined in the Rewards interface:

-   `issue_reward`: For this instance issues a randomized cashback based reward coupon that is added to the rewards of the special member

## Testing

This project includes a suite of unit tests for the classes, implemented using the `unittest` framework. To run the tests, simply run the `test.py` file:

```python test.py``` 

## Contributing

Contributions to this project are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE).