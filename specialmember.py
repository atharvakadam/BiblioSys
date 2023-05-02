from book import Book
from cashbackrewards import CashbackRewards
from discountrewards import DiscountRewards
from member import Member
from subscriptionrewards import SubscriptionRewards

class SpecialMember(Member):
    """
    A class representing a special library member who earns reward points for returning books on time.
    Inherits from the Member class.

    Attributes:
    -----------
    __member_id : str
        The unique ID of the member.
    __name : str
        The name of the member.
    __address : str
        The address of the member.
    __phone_number : str
        The phone number of the member.
    __books_issued : dict
        A dictionary of books currently borrowed by the member.
        The keys are Book objects and the values are due dates represented as datetime objects.
    __rewards : list
        A list of rewards earned by the member.
        Each reward is a string representing a reward coupon.

    Methods:
    --------
    return_book(book_obj)
        Updates the books_borrowed dictionary and adds reward points for returning the book on time.
    add_reward()
        Adds a randomized reward coupon to the rewards list.
    """

    def __init__(self, name: str, address: str, phone_number: str, member_id: str):
        """
        Constructs a SpecialMember object with the given name, age, address, phone number and member ID.
        Initializes the __books_issued list and __rewards_claimed list.

        Parameters:
        -----------
        (Data members inherited from Member class)
        __name : str
            The name of the member.
        __address : str
            The address of the member.
        __phone_number : str
            The phone number of the member.
        __member_id : str
            The unique ID of the member.

        (Data members defined exclusively for SpecialMember class):
        __reward_points : int
            The number of reward points earned so far by the special member
        __rewards_claimed: list
            The rewards claimed so far
        """
        super().__init__(member_id, name, address, phone_number)
        self.__reward_points = 200
        self.__rewards_claimed = []

    def __str__(self) -> str:
        """
        Prints out the title, author, publication year, and ISBN of the book.
        """
        return  f"Member Id: {self.get_member_id()} \n" + \
                f"Name: {self.get_name()} \n" + \
                f"Address: {self.get_address()} \n" + \
                f"Phone : {self.get_phone()} \n" + \
                f"Books Issued : {self.get_books_issued()} \n" + \
                f"Reward Points: {self.__reward_points} \n" + \
                f"Rewards Claimed: {self.__rewards_claimed} \n" \
                
    
    def get_reward_points(self) -> int:
        return self.__reward_points
    
    def get_all_won_rewards(self) -> list:
        return self.__rewards_claimed

    def increment_reward_points(self, points):
        self.__reward_points += points

    def return_book(self, book: Book) -> None:
        """
        Updates the books_borrowed dictionary and adds reward points for returning the book on time.

        Parameters:
        -----------
        book_obj : Book object
            The Book object to be returned by the member.
        """
        if book in self.get_books_issued():
            # remove book from issued books
            self.remove_book_issued(book)
            self.__reward_points += 10
        else:
            print(f"{self.get_name()} did not borrow {book.get_title()} from this library.")

    def redeem_reward(self, type_of_reward) -> None:
        """
        Member can redeem a reward for every 200 points met. After claiming the reward, it is added to the __rewards_claimed list and 
        200 points are deducted.

        Parameters:
        -----------
        type_of_reward : str 
            The type of reward can be either subscription, discount or cashback. Based on input, a reward of that type will be awarded.
        """
        try:
            if self.__reward_points < 200:
                raise ValueError(f"Not enough reward points to redeem reward. {200 - self.__reward_points} more points till next reward " )
            reward_coupon = {'subscription': SubscriptionRewards().issue_reward(), 
                            'discount':DiscountRewards().issue_reward(),
                            'cashback':CashbackRewards().issue_reward()}
            self.__reward_points -= 200
            self.__rewards_claimed.append(reward_coupon[type_of_reward])
        except ValueError as e:
            print(e)